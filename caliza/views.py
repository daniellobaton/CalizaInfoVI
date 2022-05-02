from cmath import log
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json

# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.getCartItems
    else:
        items = []
        order = {'getCartTotal': 0, 'getCartItems': 0, 'shipping': False}
        cartItems = order['getCartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'caliza/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.getCartItems
    else:
        items = []
        order = {'getCartTotal': 0, 'getCartItems': 0, 'shipping': False}
        cartItems = order['getCartItems']


    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'caliza/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.getCartItems

    else:
        items = []
        order = {'getCartTotal': 0, 'getCartItems': 0, 'cartItems': cartItems, 'shipping': False}
        cartItems = order['getCartItems']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'caliza/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Product id: ', productId)
    print('Action: ', action)

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

def processOrder():
    return JsonResponse('Payment complete', safe=False)