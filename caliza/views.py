from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import json
import datetime
from .models import *
from . utils import cookieCart, cartData, guestOrder

# Import pagination stuff
from django.core.paginator import Paginator

# Create your views here.
def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'caliza/store.html', context)

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'caliza/cart.html', context)

def wishList(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {'items': items, 'order': order, 'cartItems': cartItems, 'products': products}
    return render(request, 'caliza/wishList.html', context)

def loginUser(request):
    
    if request.method == "POST":
        # print(f"estás en el post")
        form = AuthenticationForm(request, data = request.POST)
        # print(f"{form}")
        if form.is_valid():
            user = form.cleaned_data.get('username')
            key = form.cleaned_data.get('password')
            credentials = authenticate(username = user, password = key)
            
            # print(f"acceso válido")
            print(f"{credentials}")
            
            if credentials is not None:
                login(request, credentials)
                messages.info(request, f"Estás logueado como {user}")
                return redirect('store')
            else:
                messages.error(request, "Usuario o clave incorrectos")
        else:
            # print(f"acceso no válido")
            messages.error(request, "Usuario o clave incorrectos")
    # messages.info(request, f"mensaje {user}")
      
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'caliza/loginUser.html', context)

def signIn(request):
    return render(request, 'caliza/signIn.html')

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'caliza/checkout.html', context)

def ourProducts(request):
    data = cartData(request)
    cartItems = data['cartItems']
    productsList = Product.objects.all()
    
    # Set up pagination
    pagination = Paginator(Product.objects.all(), 9)
    page = request.GET.get('page')
    products = pagination.get_page(page)
    nums = "a" * products.paginator.num_pages
    
    context = {'productsList': productsList, 'products': products, 'nums': nums, 'cartItems': cartItems}
    return render(request, 'caliza/ourProducts.html', context)
    
def individualProduct(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'caliza/individualProduct.html', context)    

def promos(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'caliza/promos.html', context)  

def masVendidos(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'caliza/masVendidos.html', context) 

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action: ', action)
    print('Product id: ', productId)
    
    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)

    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

#from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt
def processOrder(request):
    transactionId = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transactionId = transactionId

    if total == order.getCartTotal:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(

            customer = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipCode = data['shipping']['zipcode'],
        )

    return JsonResponse('Payment complete', safe=False)