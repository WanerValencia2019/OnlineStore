from django.db import models

from django.contrib.auth import get_user_model
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

    
