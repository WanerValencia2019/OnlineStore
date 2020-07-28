import decimal
import uuid
from django.db import models
from django.db.models.signals import pre_save, m2m_changed,post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model



from .managers import CartProductsManager
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

    DISCOUNT = 0.3

    def __str__(self):
        return "{}".format(self.cart_id)
    
    @property
    def select_related(self):
        return self.cartproducts_set.select_related('product')

    @property
    def countProducts(self):
        return self.cartproducts_set.select_related('product').count()

    
    def updatePrice(self):
        self.updateSubtotal()
        self.updateTotal()

    def updateSubtotal(self):
        self.subtotal = sum([(c.product.price * c.quantity)  for c in self.cartproducts_set.select_related('product')])
        self.save()

    def updateTotal(self):
        self.total = self.subtotal - self.get_discount()
        self.save()

    def get_discount(self):
        discount = self.subtotal * decimal.Decimal(self.DISCOUNT)
        return discount.quantize(decimal.Decimal('1.00'))



class CartProducts(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CartProductsManager()


    def __str__(self):
        return "{}".format(self.cart.cart_id)



@receiver(pre_save,sender=Cart)
def set_cart_id(instance,*args, **kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())

@receiver(pre_save,sender=CartProducts)
def updatePrice(instance,*args, **kwargs):
    instance.price = instance.product.price * instance.quantity
    print(instance.price)
    
@receiver(post_save,sender=CartProducts)
def updateQuantity(instance,*args, **kwargs):
    instance.cart.updatePrice()
    

@receiver(m2m_changed,sender=Cart.products.through)
def set_price(sender,instance,action,*args, **kwargs):
    print(action)
    if action=='post_add' or action=='post_remove' or action=='post_clear':
        instance.updatePrice()





