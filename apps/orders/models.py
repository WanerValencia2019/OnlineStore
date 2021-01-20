from enum import Enum
from decimal import Decimal
from uuid import uuid4

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
# Create your models here.

from apps.carts.models import Cart

from apps.shipping_adress.models import ShippingAdress 

UserModel = get_user_model()

class OrderStatus(Enum):
    CREATED='CREATED'
    PAYED='PAYED'
    COMPLETED='COMPLETED'
    CANCELED='CANCELED'

choices = [(tag, tag.value) for tag in OrderStatus]


class Order(models.Model):
    order_id = models.CharField(max_length=150,null=False,blank=False,unique=True)
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,verbose_name='Usuario')
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    status = models.CharField(max_length=50,choices=choices,default=OrderStatus.CREATED)
    shipping_total = models.DecimalField(max_digits=6,decimal_places=2,default=5500.0)
    total = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    shipping_adress = models.ForeignKey(ShippingAdress, null=True, blank=True, on_delete=models.CASCADE)


    @property
    def total_to_pay(self):
        total = Decimal(Decimal(self.cart.total) + Decimal(self.shipping_total))
        self.total = total.quantize(Decimal(1.000))
        self.save()

    def __str__(self):
        return self.order_id


    def get_or_create_shipping_adress(self):
        if self.shipping_adress:
            return self.shipping_adress

        shipping_adress = self.user.shipping_adress
    
        if shipping_adress:
            self.update_shipping_adress(shipping_adress)

        return shipping_adress

    def update_shipping_adress(self, shipping_adress):
        self.shipping_adress = shipping_adress
        self.save()        


@receiver(pre_save,sender=Order)
def set_order_id(instance,*args, **kwargs):
    if not instance.order_id:
        instance.order_id = str(uuid4())
        instance.total_to_pay