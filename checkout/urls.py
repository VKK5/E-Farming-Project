from django.urls import path,include
from . import views

urlpatterns = [
  
    path('addrandpay/', views.payform, name='addrandpay'),  
    path('thankyou/', views.thanks, name='thankyou'),
]