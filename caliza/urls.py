from django.urls import path
from . import views

urlpatterns = [

    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('ourProducts/', views.ourProducts, name='ourProducts'),
    
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('individual_product/', views.individual, name='individual_product'),
    path('promos/', views.promos, name='promos'),
    path('masVendidos/', views.masVendidos, name='masVendidos'),
]