from django.shortcuts import render, redirect, get_object_or_404
from bazaar.models import Product
from .models import Cart,Order
from django.contrib import messages
from django.http import HttpResponse

""" from django.views.decorators.http import require_POST
from .forms import CartAddProductForm """

# Create your views here.

""" 
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})

 """







def add_to_cart(request, product_id):
    item = get_object_or_404(Product, id=product_id)
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
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
    cart_qs = Cart.objects.filter(user=request.user, item=item)
    if cart_qs.exists():
        cart = cart_qs[0]
        # Checking the cart quantity
        """ if cart.quantity > 1:
            cart.quantity = 0
            cart.save()
        else: """
        cart_qs.delete()
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__id=item.id).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user,
            )[0]
            order.orderitems.remove(order_item)
           # messages.info(request, "This item was removed from your cart.")
            return redirect('carthome')
        else:
           # messages.info(request, "This item was not in your cart")
            return redirect("carthome")
    else:
       # messages.info(request, "You do not have an active order")
        return redirect("carthome")


def decreaseCart(request, product_id):
    item = get_object_or_404(Product, id=product_id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__id=item.id).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
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

    carts = Cart.objects.filter(user=user)
    orders = Order.objects.filter(user=user, ordered=False)

    if carts.exists():
        order = orders[0]
        return render(request, 'cart/carthome.html', {"carts": carts, 'order': order})
		
    else:
       # messages.warning(request, "You do not have an active order")
        return render(request, 'cart/carthome.html',{"carts":{}})
        #return redirect('carthome')
       # return HttpResponse("<h1>Your Cart</h1>No items to show")