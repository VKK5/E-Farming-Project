from django import template
from cart.models import Order

register = template.Library()

@register.filter
def cart_total(user):
    order = Order.objects.filter(user=user, ordered=False)

    if order.exists():
    	return order[0].orderitems.count()
    else:
    	return 0

@register.filter
def myorders_total(user):

    myorders = Order.objects.filter(user=user, ordered=True)

    if myorders.exists():
        return len(myorders)

    else:
        return 0