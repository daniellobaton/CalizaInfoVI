from django.shortcuts import render

# Create your views here.
def store(request):
    context = {}
    return render(request, 'caliza/store.html', context)

def cart(request):
    context = {}
    return render(request, 'caliza/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'caliza/checkout.html', context)