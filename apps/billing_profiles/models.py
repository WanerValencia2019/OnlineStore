from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
from .managers import BillingProfilesManager

UserModel = get_user_model()

class BillingProfiles(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    token = models.CharField(max_length=50, null=False, blank=False)
    card_id = models.CharField(max_length=50, null=False, blank=False)
    last4 = models.CharField(max_length=50, null=False, blank=False)
    brand = models.CharField(max_length=50, null=False, blank=False)
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = BillingProfilesManager()

    def __str__(self):
        return "{} - {}".format(self.user.get_full_name(),self.card_id)
    
    class Meta:
        verbose_name = 'Perfiles de pago'
        verbose_name_plural = 'Perfiles de pagos'
        

@receiver(post_save, sender=BillingProfiles)
def stablishDefaultBilling(sender,instance,**kwargs):
    default = instance.default
    pk = instance.pk
    print("ACTUALIZANDO LOS DEFAULT EN BILLING PROFILE")
    if default == True:
        defaults = BillingProfiles.objects.exclude(default=False).exclude(pk=pk)
        print(defaults)
        for d in defaults:
            d.default = False
        BillingProfiles.objects.bulk_update(defaults, ['default'])
    
