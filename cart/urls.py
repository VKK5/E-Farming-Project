from django.urls import path,include
from . import views


urlpatterns = [
  
    path('addtocart/<int:product_id>', views.add_to_cart, name='addtocart'),
    path('removefromcart/<int:product_id>', views.remove_from_cart, name='removefromcart'),
    path('carthome/', views.CartView, name='carthome'),
    path('decreasecart/<int:product_id>', views.decreaseCart, name='decreasecart'),
]