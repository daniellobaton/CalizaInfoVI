from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import json
import datetime
from .models import *
from . utils import cookieCart, cartData, guestOrder, individualPurchase
from . forms import SignInUserForm

# Import pagination stuff
from django.core.paginator import Paginator

# Create your views here.
def store(request):
    # print(request.user.is_authenticated)
    dataCart = cartData(request)
    cartItems = dataCart['cartItems']
    customer = dataCart['customer']
    
    try:
        
        productsWishList = GetProducts.objects.get(customer = customer)
    
    except:
        
        productsWishList = {}

    products = Product.objects.all()[:6]
    
    if request.user.is_authenticated:
        
        context = {'products': products, 'productsWishList': productsWishList, 'cartItems': cartItems}
        
    else:
        
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
    
    customer = request.user.customer
    
    #Devolver productos:
    products = GetProducts.objects.filter(customer = customer).values()
    
    #Diccionario que se enviará al HTML
    producto = []
    
    for i in range(len(products)):
        #Obtenemos el id de cada producto en el diccionario products
        productId = products[i]['product_id']

        #Traemos de la BD el producto con el id del renglón anterior
        producto.append(Product.objects.get(id = productId)) 

    context = {'items': items, 'order': order, 'cartItems': cartItems, 'products': producto}
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
    
    # ultimoCustomer = Customer.objects.all().order_by('-id')[0]
    ultimoUser = User.objects.all().order_by('-id')[0]
    numeroCustomers = Customer.objects.count()
    numeroUsers = User.objects.count()
    
    if numeroUsers > numeroCustomers:

        Customer.objects.create(
            user = ultimoUser,
            name = ultimoUser.username,
            email = ultimoUser.email
        )
        return redirect('store')
        # isAuthenticated = True
    
    if request.method == "POST":

        print('POST activado')

        form = SignInUserForm(request.POST)
        # print(f"{form}")
        if form.is_valid():
            formSave = form.save()
            
            Customer.objects.create(
                user = formSave,
                name = formSave.username,
                email = formSave.email
            ) 
            
            user = form.cleaned_data['username']
            key = form.cleaned_data['password1']
            credentials = authenticate(username=user, password=key)
            
            
            login(request, credentials)
            
            messages.success(request, ("Registro exitoso"))
            return redirect('store')
    else: 
        form = SignInUserForm()

    context = {'form': form}
    return render(request, 'caliza/signIn.html', context)

def checkout(request):

    if request.GET:
        productId = request.GET['producto']
        cantidad = request.GET['cantidad']
        #print('Todo correcto!')
        #print(productId)
        #print(cantidad)
        iterable = False

        producto = Product.objects.get(id = productId)
        #print(producto.price)
        #print(cantidad)
        #total = 0
        total = int(producto.price) * int(cantidad)
        datos = individualPurchase(request)
        order = datos['order'] 

        context = {'items': producto, 'quantity': cantidad, 'iterable': iterable, 'total': total, 'order': order}
    else:

        data = cartData(request)
        cartItems = data['cartItems']
        order = data['order']
        items = data['items'] #arreglo con los productos del carrito
        iterable = True

        context = {'items': items, 'order': order, 'cartItems': cartItems, 'iterable': iterable}

    return render(request, 'caliza/checkout.html', context)

def ourProducts(request):

    hayCategoria = False
    categoria = None

    if request.GET:
        hayCategoria = True
        categoria = request.GET['categoria']

    data = cartData(request)
    cartItems = data['cartItems']
    productsList = Product.objects.all()
    # Set up pagination
    pagination = Paginator(Product.objects.all(), 9)
    page = request.GET.get('page')
    products = pagination.get_page(page)
    nums = "a" * products.paginator.num_pages
    
    context = {'productsList': productsList, 'products': products, 'nums': nums, 'cartItems': cartItems, 'hayCategoria': hayCategoria, 'categoria': categoria}
    return render(request, 'caliza/ourProducts.html', context)
    
def individualProduct(request):
    #print(request.GET)
    productId = request.GET['producto']
    product = Product.objects.get(id = productId)
    #print('Precio del producto: ', product.price)
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems, 'producto': product}
    return render(request, 'caliza/individualProduct.html', context)

def promos(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    productos = Oferta.objects.all()[:5]

    context = {'items': items, 'order': order, 'cartItems': cartItems, 'productos': productos}
    return render(request, 'caliza/promos.html', context)  

def masVendidos(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    products = Product.objects.all()[:10]

    context = {'items': items, 'order': order, 'cartItems': cartItems,'products': products}
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

def deleteItems(request):
    data = json.loads(request.body)
    productId = data['productId']
    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)
   
    orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def updateWishList(request):
    data = json.loads(request.body)
    print(data)
    productId = data['productId']
    action = data['action']

    print('Action: ', action)
    print('Product id: ', productId)
    
    customer = request.user.customer
    product = Product.objects.get(id = productId)
    productsList, created = GetProducts.objects.get_or_create(customer = customer, product = product)

    productsList.save()

    return JsonResponse('Item was added', safe=False)

def deleteWishListItem(request):
    data = json.loads(request.body)
    print(data)
    productId = data['productId']
    iteration = data['iteration']

    registro = GetProducts.objects.filter(id=iteration)
    #print(registro)

    registro.delete()

    return JsonResponse('Item was deleted', safe=False)

#from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt
def processOrder(request):
    data = cookieCart(request)
    items = data['items']

    #print('productos: ', items[0]['product']['id'])

    transactionId = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    print("Datos: ", data)

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
