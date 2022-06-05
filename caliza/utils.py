import json
from . models import *

def cookieCart(request):

    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    items = []
    order = {'getCartTotal': 0, 'getCartItems': 0, 'shipping': False}
    cartItems = order['getCartItems']

    for i in cart:

        try:

            cartItems += cart[i]["quantity"]

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['getCartTotal'] += total
            order['getCartItems'] += cart[i]['quantity']


            item = {
                'product':{
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                },
                'quantity': cart[i]['quantity'],
                'getTotal': total
            }

            items.append(item)

            if product.digital == False:
                order['shipping'] = True

        except:
            pass

    return {'cartItems': cartItems, 'order': order, 'items': items}


def cartData(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.getCartItems

    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        customer = None
        
        order = cookieData['order']
        items = cookieData['items']

    return {'cartItems': cartItems, 'order': order, 'items': items, 'customer': customer}

# def wishListData(request):
    
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         request.product
#         print(f"items de wishlist: {wishListItems}")

    # return {'order': order, 'wishListItems': wishListItems}

def individualPurchase(request):
    if request.user.is_authenticated:
        productId = request.GET['producto']
        product = Product.objects.get(id = productId)
        cantidad = request.GET['cantidad']
        total = int(product.price) * cantidad
        #print('producto: ', product)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        
    else:
        productId = request.GET['producto']
        product = Product.objects.get(id = productId)
        cantidad = request.GET['cantidad']
        total = int(product.price) * cantidad
        order = {}

    item = {
            'product':{
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'imageURL': product.imageURL,
            },
            'quantity': cantidad,
            'getTotal': total
    }

    #if product.digital == False:
      #  order['shipping'] = True

    return {'item': item, 'order': order}
    #return {'order': order}


def guestOrder(request, data):

    print('User is not logged in')

    print('COOKIES:', request.COOKIES)
    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(
        email = email,
    )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer = customer,
        complete = False,
    )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])

        orderItem = OrderItem.objects.create(
            product = product,
            order = order,
            quantity = item['quantity']                
        )

    return customer, order


def borraItemCarrito(request):
    if request.user.is_authenticated:
        print('Usuario autenticado')
        # productId = request.GET['producto']
        # product = Product.objects.get(id = productId)
        # cantidad = request.GET['cantidad']
        # total = int(product.price) * cantidad
        # #print('producto: ', product)
        # customer = request.user.customer
        # order, created = Order.objects.get_or_create(customer = customer, complete = False)
        
    else:
        print('Usuario no autenticado')
        # productId = request.GET['producto']
        # product = Product.objects.get(id = productId)
        # cantidad = request.GET['cantidad']
        # total = int(product.price) * cantidad
        # order = {}
