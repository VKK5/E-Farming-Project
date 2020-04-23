from django.shortcuts import render
from .models import Product
from django.views import generic
#from cart.forms import CartAddProductForm

# Create your views here.



def bazhome(request):
    return render(request, 'bazaar/bazhome.html')

def bazabout(request):
    return render(request, 'bazaar/bazabout.html')



def bazproducts(request):

    prods = Product.objects.all()

    return render(request,'bazaar/bazproducts.html',{'prods':prods})
    

def proddetails(request,prodid):
    
    prod = Product.objects.get(pk=prodid)

    #cart_product_form = CartAddProductForm()
    #return render(request,'bazaar/bazindex.html',{'product':prod,'cart_product_form':cart_product_form})
    return render(request,'bazaar/proddetails.html',{'product':prod})    






"""
class bazproductsview(generic.ListView):
    template_name = 'bazaar/bazproducts.html'

    def get_queryset(self):
        return Product.objects.all()

class detailsview(generic.DeleteView):
    model = Product
    template_name = 'bazaar/proddetails.html'

"""

