import email
import pytest
from caliza.models import *

@pytest.mark.django_db
def test_product_creation():
	
    producto = Product.objects.create(

        name = '',
        price = 5.7,
        digital = True,  
    )

    assert producto.name != '' and producto.price <= 50000 and producto.price > 0

@pytest.mark.django_db
def test_address_creation():
    direccion = ShippingAddress.objects.create(
            customer = Customer.objects.create(),
            order = Order.objects.create(),
            address = '',
            city = '',
            state = '',
            zipCode = '',
        )
    assert direccion.customer != None and direccion.order != None and direccion.address != '' and direccion.city != '' and direccion.state != '' and direccion.zipCode != ''

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