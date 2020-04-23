from django.urls import path,include
from . import views

#app_name='bazaar'

urlpatterns = [
    path('',views.bazhome, name='bazhome'),
    path('bazhome',views.bazhome, name='bazhome'),
    path('bazabout/',views.bazabout, name='bazabout'),

   # path('bazproducts/', views.bazproductsview.as_view(), name='bazproducts'),
    path('bazproducts/',views.bazproducts,name='bazproducts'),
    path('bazproducts/proddetails/<int:prodid>',views.proddetails, name='proddetails'),
   # path('accounts/',include('accounts.urls')),
   # path('cart/',include('cart.urls')),

    #path('bazproducts/proddetails/<pk>',views.detailsview.as_view(), name='proddetails'),
]

