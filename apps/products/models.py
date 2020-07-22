from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
#MANAGER CUSTOM
from .managers import ProductManager

# Create your models here.
class Product(models.Model):
    title = models.CharField(verbose_name='Nombre',max_length=50)
    image = models.ImageField(verbose_name='Imagen descriptiva',upload_to='products/',null=True,blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    slug = models.SlugField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)
    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})
        
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
        ordering= ['title']

@receiver(pre_save,sender=Product)
def set_slug(instance,*args, **kwargs):
    instance.slug = slugify(instance.title)

