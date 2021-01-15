from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Q

UserModel = get_user_model()
# Create your models here.
class ShippingAdress(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    line1 = models.CharField(max_length=50, verbose_name='Carrera')
    line2 = models.CharField(max_length=50, verbose_name='Calle')
    city = models.CharField(max_length=50,verbose_name='Ciudad')
    state = models.CharField(max_length=50, verbose_name='Departamento')
    country = models.CharField(max_length=50, verbose_name='País')
    reference = models.CharField(max_length=150, verbose_name='Referencia')
    postal_code = models.CharField(max_length=10,verbose_name='Código postal')
    cellphone = models.CharField(max_length=12,verbose_name='Número telefónico')
    default = models.BooleanField(verbose_name='Por defecto',default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name='Dirección de envio'
        verbose_name_plural='Direcciones de envio'
        ordering= ['default','created_at']

@receiver(post_save, sender=ShippingAdress)
def stablishDefaultAdress(sender,instance,**kwargs):
    default = instance.default
    pk = instance.pk
    print("ACTUALIZANDO LOS DEFAULT EN DIRECCION")
    if default == True:
        print(instance.user)
        print(pk)
        defaults = ShippingAdress.objects.exclude(default=False).exclude(pk=pk)
        print(defaults)
        for d in defaults:
            d.default = False
        ShippingAdress.objects.bulk_update(defaults, ['default'])
        
