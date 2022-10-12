import email
import pytest
from caliza.models import *

####Creación producto con precio negativo
@pytest.mark.django_db
def test_precio_negativo():
    producto = Product.objects.create(

        name = '',
        price = -5,
        imageURL = ''
    )
    assert producto != None

####Creación producto sin imageURL
@pytest.mark.django_db
def test_imagen_no_url():
    producto = Product.objects.create(

        name = '',
        price = -5

    )
    assert producto != None

####Orden sin customer
@pytest.mark.django_db
def test_creacion_orden():
    order, created = Order.objects.get_or_create(complete = False)
    assert order != None

####Variable get incorrecta en producto individual o en promociones
@pytest.mark.django_db
def test_get_method():
    producto = Product.objects.get(id = 'x')
    assert producto != None

@pytest.mark.django_db
def test_address_creation():
    customer = Customer.objects.create(
                user = User.objects.create(),
                name = '',
                email = '',
            )

    direccion = ShippingAddress.objects.create(
            customer = customer,
            order = Order.objects.create(),
            address = '',
            city = '',  
            state = '',
            zipCode = '',
        )
    assert direccion != None

@pytest.mark.django_db
def test_customer_creation():
    customer = Customer.objects.create(
            user = User.objects.create(),
            name = '',
            email = '',
        )
    assert customer.user != None and customer.name != '' and customer.email != ''

@pytest.mark.django_db
def test_product_creation2():
	
    producto = Product.objects.create(

        name = 'Limpiapisos',
        price = 67.5,
        digital = True,  
    )

    assert producto.name != '' and producto.price <= 50000 and producto.price > 0

@pytest.mark.django_db
def test_address_creation2():
    direccion = ShippingAddress.objects.create(
            customer = Customer.objects.create(),
            order = Order.objects.create(),
            address = 'C.U. 5422',
            city = 'Coyoacán',
            state = 'CDMX',
            zipCode = '56988',
        )
    assert direccion.customer != None and direccion.order != None and direccion.address != '' and direccion.city != '' and direccion.state != '' and direccion.zipCode != ''

@pytest.mark.django_db
def test_customer_creation2():
    customer = Customer.objects.create(
            user = User.objects.create(),
            name = 'Daniel',
            email = 'daniellobaton@outlook.com',
        )
    assert customer.user != None and customer.name != '' and customer.email != ''