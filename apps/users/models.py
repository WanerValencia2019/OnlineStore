from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='Correo electrónico',unique=True)

    @property
    def shipping_adress(self):
        return self.shippingadress_set.filter(default=True).first()

# Create your models here.
