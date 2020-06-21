from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from cart.models import Order

# Create your models here.

User = get_user_model()

paymenttype = [
    ('NETBANKING','netbanking'),
    ('PAYPAL','paypal'),
    ('PAYTM','paytm'),
    ('MASTERCARD','mastercard'),
    ('VISACARD','visacard'),
]


class Addressandpayment(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    order_id = models.IntegerField()
    paymenttype = models.CharField(max_length = 20, choices=paymenttype)
    accountnumber = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=50)
    city = models.CharField(max_length=30)


    def __str__(self):
        return f'Order id {self.order_id} of {self.user.username} Payment Details and Billing Address'



class AddressandpaymentForm(ModelForm):
    class Meta:
        model = Addressandpayment
        fields = ['paymenttype','accountnumber','address','zipcode','city']





