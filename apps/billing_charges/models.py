from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from apps.orders.models import Order
from .managers import BillingChargeManager
UserModel = get_user_model()

class BillingCharge(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name="Usuario")
    order = models.OneToOneField(Order, verbose_name="Orden", on_delete=models.CASCADE)
    #Stripe envia los siguentes campos
    charge_id=models.CharField(max_length=100)
    amount = models.IntegerField("Dinero a pagar",default=0)#STripe acepta el valor en centavos, toca convertirlo
    payment_method = models.CharField("Metódo de pago", max_length=100)#id card
    status = models.CharField("Estado", max_length=50)
    created_at = models.DateField(auto_now_add=True)
    objects = BillingChargeManager()
    def __str__(self):
        return self.charge_id

