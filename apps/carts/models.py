import uuid
from django.db import models
from django.db.models.signals import pre_save, m2m_changed
from django.dispatch import receiver

from apps.products.models import Product
# Create your models here.

class Cart(models.Model):
    cart_id = models.UUIDField(default=uuid.uuid4,editable=False)
    products = models.ManyToManyField(Product,related_name='carts_products',through='CartProducts')
    subtotal =  models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    total = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartProducts(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.cart