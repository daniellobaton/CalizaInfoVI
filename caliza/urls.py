from django.urls import path
from . import views

urlpatterns = [

    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('wishList/', views.wishList, name='wishList'),
    path('loginUser/', views.loginUser, name='loginUser'),
    path('signIn/', views.signIn, name='signIn'),
    path('logoutUser/', views.logoutUser, name='logoutUser'),
    path('checkout/', views.checkout, name='checkout'),
    path('ourProducts/', views.ourProducts, name='ourProducts'),
    
    path('update_item/', views.updateItem, name='update_item'),
    path('delete_items/', views.deleteItems, name='delete_items'),
    path('update_wishList/', views.updateWishList, name='update_wishList'),
    path('delete_wishList/', views.deleteWishListItem, name='delete_wishList'),
    path('process_order/', views.processOrder, name='process_order'),
    path('individualProduct/', views.individualProduct, name='individual_product'),
    path('promos/', views.promos, name='promos'),
    path('masVendidos/', views.masVendidos, name='masVendidos'),
]
