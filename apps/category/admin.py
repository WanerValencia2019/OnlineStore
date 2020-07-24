from django.contrib import admin

from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal = ('products',)

admin.site.register(Category,CategoryAdmin)
