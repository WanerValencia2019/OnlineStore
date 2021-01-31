import string
import random
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.

from .managers import PromoCodesManager

class PromoCodes(models.Model):
    code = models.CharField(max_length=50,verbose_name="Código promocional")
    discount = models.FloatField(verbose_name="Descuento", default=0.0)
    valid_from = models.DateTimeField(verbose_name="Válido de")
    valid_to = models.DateTimeField(verbose_name="Válido hasta")
    used=models.BooleanField(verbose_name="Usado", default=False)
    objects = PromoCodesManager()

    def __str__(self):
        return "{}".format(self.code)
    
    def setUsed(self):
        self.used = True
        self.save()

    class Meta:
        verbose_name = "Código promocional"
        verbose_name_plural = 'Códigos promocionales'
        ordering = ['code',]

@receiver(pre_save, sender=PromoCodes)
def setCode(sender, instance, *args, **kwargs):
    if not instance.code:
        charts = string.ascii_uppercase + string.digits
        code = ''.join(random.choice(charts) for w in range(14))
        print(code)
        instance.code =code
        instance.save()