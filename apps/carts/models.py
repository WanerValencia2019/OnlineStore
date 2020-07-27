import uuid
from django.db import models
from django.db.models.signals import pre_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from apps.products.models import Product
# Create your models here.

UserModel = get_user_model()

class Cart(models.Model):
    cart_id = models.CharField(max_length=100,null=False)
    user = models.ForeignKey(UserModel,null=True,blank=True,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,related_name='cart_products',through='CartProducts')
    subtotal =  models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    total = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.cart_id)
    
    @property
    def select_related(self):
        return self.cartproducts_set.select_related('product')

    @property
    def countProducts(self):
        return self.cartproducts_set.select_related('product').count()
        
@receiver(pre_save,sender=Cart)

def set_cart_id(instance,*args, **kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())

class CartProducts(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "{}".format(self.cart.cart_id)