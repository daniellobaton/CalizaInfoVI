from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'caliza/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'getCartTotal': 0, 'getCartItems': 0}

    context = {'items': items, 'order': order}
    return render(request, 'caliza/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'getCartTotal': 0, 'getCartItems': 0}

    context = {'items': items, 'order': order}
    return render(request, 'caliza/checkout.html', context)