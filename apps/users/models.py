from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='Correo electrónico',unique=True)

# Create your models here.
