from django.db import models
from apps.products.models import Product
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50,verbose_name='Titulo')
    products = models.ManyToManyField(Product,verbose_name='Productos',related_name='category_products')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Categoría'
        verbose_name_plural = 'Categorías'