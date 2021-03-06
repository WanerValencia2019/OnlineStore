import decimal
import uuid
from django.db import models
from django.db.models.signals import pre_save, m2m_changed,post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model



from .managers import CartProductsManager
from apps.products.models import Product
from apps.promo_codes.models import PromoCodes
# Create your models here.

UserModel = get_user_model()


class Cart(models.Model):
    cart_id = models.CharField(max_length=100,null=False)
    user = models.ForeignKey(UserModel,null=True,blank=True,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,related_name='cart_products',through='CartProducts')
    subtotal =  models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    total = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    promoCode = models.OneToOneField(PromoCodes,on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    DISCOUNT = 0.0

    class Meta:  
        verbose_name = 'Carrito de compra'
        verbose_name_plural = 'Carrito de compras'

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
        if self.order_set.first():
            self.order_set.first().total_to_pay

    def updateSubtotal(self):
        self.subtotal = sum([(c.product.price * c.quantity)  for c in self.cartproducts_set.select_related('product')])
        self.save()

    def apply_code_promo(self, promo_code):
        if self.promoCode is None:
            self.promoCode = promo_code
            self.save()
    

            self.updateTotal()
            promo_code.setUsed()

    def updateTotal(self):
        self.total = self.subtotal - self.get_discount() 
        self.save()

    def get_discount(self):
        discount = self.subtotal * decimal.Decimal(self.DISCOUNT) +  (decimal.Decimal(self.promoCode.discount) if self.promoCode else decimal.Decimal(0))
        return discount.quantize(decimal.Decimal('1.00'))
        return decimal.Decimal(0.0)
    
    @property
    def order(self):
        return self.order_set.first()
        



class CartProducts(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    price = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CartProductsManager()


    def __str__(self):
        return "{}".format(self.cart.cart_id)
    class Meta:
        verbose_name = 'Producto del carrito'
        verbose_name_plural = 'Productos del carrito'



@receiver(pre_save,sender=Cart)
def set_cart_id(instance,*args, **kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())


@receiver(pre_save,sender=CartProducts)
def updatePrice(instance,*args, **kwargs):
    instance.price = instance.product.price * instance.quantity
    
    
@receiver(post_save,sender=CartProducts)
def updateQuantity(instance,*args, **kwargs):
    instance.cart.updatePrice()
   
    

@receiver(m2m_changed,sender=Cart.products.through)
def set_price(sender,instance,action,*args, **kwargs):
    print(action)
    if action=='post_add' or action=='post_remove' or action=='post_clear':
        instance.updatePrice()





