from django.shortcuts import render, redirect, get_object_or_404
from bazaar.models import Product
from .models import Cart,Order
from checkout.models import Addressandpayment
from django.contrib import messages
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required


#Add item to cart

@login_required(login_url='login')
def add_to_cart(request, product_id):
    item = get_object_or_404(Product, id=product_id)
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user,
        purchased=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
     #   print('add to cart')
     #   print (order_qs, '----------------------------------',type(order_qs), '>>>>>>>>>>>>>>>', order_qs[0])
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__id=item.id).exists():
            
            order_item.quantity += 1
            order_item.save()
            #messages.info(request, "This item quantity was updated.")
            return redirect('carthome')
        else:
            order.orderitems.add(order_item)
            #messages.info(request, "This item was added to your cart.")
            return redirect('carthome')
    else:
        order = Order.objects.create(
            user=request.user)
        order.orderitems.add(order_item)
        #messages.info(request, "This item was added to your cart.")
        return redirect('carthome')






# Remove item from cart

def remove_from_cart(request, product_id):

    item = get_object_or_404(Product, id=product_id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__id=item.id).exists():
           # print('------HI------')
            order_item = Cart.objects.filter(
                item=item,
                user=request.user,
                purchased=False
            )[0]
            if order_item.quantity >= 1:
                order.orderitems.remove(order_item)
                order_item.delete()
            if order.get_totals()==0:
                order_qs[0].delete() 

           # messages.info(request, f"{item.name} quantity has updated.")
            return redirect('carthome')
        else:
           # messages.info(request, f"{item.name} quantity has updated.")
            return redirect('carthome')
    else:
      #  messages.info(request, "You do not have an active order")
        return redirect('carthome')



def decreaseCart(request, product_id):
    item = get_object_or_404(Product, id=product_id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False,
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__id=item.id).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user,
                Purchased=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
            
            if order.get_totals()==0:
                order_qs[0].delete()
            

           # messages.info(request, f"{item.name} quantity has updated.")
            return redirect('carthome')
        else:
           # messages.info(request, f"{item.name} quantity has updated.")
            return redirect('carthome')
    else:
      #  messages.info(request, "You do not have an active order")
        return redirect('carthome')





# Cart View

def CartView(request):

    user = request.user

    carts = Cart.objects.filter(user=user,purchased=False)
    orders = Order.objects.filter(user=user, ordered=False)

    if carts.exists():
       # print('carts',carts)
       # print('orders',orders,'-------orders[0]',orders[0])
        order = orders[0]
        return render(request, 'cart/carthome.html', {"carts": carts, 'order': order})
		
    else:
       # messages.warning(request, "You do not have an active order")
        return render(request, 'cart/carthome.html',{"carts":{}})
        #return redirect('carthome')
       # return HttpResponse("<h1>Your Cart</h1>No items to show")


def myorderview(request):
    user = request.user

    myorders = Order.objects.filter(user=user, ordered=True)


    if myorders.exists():

        # orders = myorders[0]

         return render(request,'cart/myorderhome.html',{"orders":myorders})

    else:

        return render(request,'cart/myorderhome.html',{"orders":{}})




def ordereditems(request, order_id):

    user = request.user

    orders = Order.objects.filter(user=user, id=order_id, ordered=True)

    items=[]
    for temp in orders:
        items+=temp.orderitems.all()

   # print(orders)

   # print(items)

    
    if items:
       # print('carts',carts)
       # print('orders',orders,'-------orders[0]',orders[0])
        order = orders[0]
        
        return render(request, 'cart/ordereditems.html', {"carts": items, 'order': order})
		
    else:
       # messages.warning(request, "You do not have an active order")
        return render(request, 'cart/ordereditems.html',{"carts":{}})
        #return redirect('carthome')
       # return HttpResponse("<h1>Your Cart</h1>No items to show")




def cancelorder(request, order_id):
    order = Order.objects.get(user=request.user, id = order_id, ordered=True)
    
    addrandpaydetails = Addressandpayment.objects.get(user=request.user, order_id = order_id)

    addrandpaydetails.delete()

    order.orderitems.all().delete()

    order.delete()

    return redirect('myorderhome')
