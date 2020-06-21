from django.shortcuts import render,redirect
from .models import AddressandpaymentForm,Addressandpayment
from cart.models import Cart,Order

# Create your views here.

def payform(request):

    if request.method == 'POST':
        
        #print('--------Its POST----------')
        """
        profile, created = Addressandpayment.objects.get_or_create(user=request.user)
        form = AddressandpaymentForm(
        request.POST or None,
        request.FILES or None,
        instance=profile,
        
        )
        """
        
        
        form = AddressandpaymentForm(request.POST)

        if form.is_valid():

            order = Order.objects.get(user=request.user, ordered=False)
            #print('-------HI--------')
            post = form.save(commit=False)
            post.user = request.user
            post.order_id = order.id
            post.save()
            return redirect('thankyou')


        else:
            #print('-----chill--------')
            context = {'form':form}
            return render(request,'checkout/addrandpay.html',context)
    else:
            #print('-------Its GET--------')
            form = AddressandpaymentForm()
            context={'form':form}
            return render(request, 'checkout/addrandpay.html', context)
    

def thanks(request):
    order = Order.objects.get(user=request.user, ordered=False)
    #print('-----------',order,'---------')
    order.ordered = True
    order.save()
    cartItems = Cart.objects.filter(user=request.user)

    
    for items in cartItems:
        items.purchased=True
        items.save()

    
    lis=[]
    lis+=order.orderitems.all()

        
    return render(request, 'checkout/thankyou.html', {"carts": lis, 'order': order})
    
    #return render(request,'checkout/thankyou.html')
    

