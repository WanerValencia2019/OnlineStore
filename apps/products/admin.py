from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    fields = ['title','image','description','price','unit']


admin.site.register(Product,ProductAdmin)
