from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'caliza/store.html', context)

def cart(request):
    context = {}
    return render(request, 'caliza/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'caliza/checkout.html', context)