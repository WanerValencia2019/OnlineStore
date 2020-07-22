from django.db import models



#MANAGER CUSTOM
from .managers import ProductManager

# Create your models here.
class Product(models.Model):
    title = models.CharField(verbose_name='Nombre',max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)
    objects = ProductManager()
    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
        ordering= ['title']