from django.contrib import admin
from .models import PromoCodes
# Register your models here.
class AdminPromoCode(admin.ModelAdmin):
    exclude=('code',)

admin.site.register(PromoCodes, AdminPromoCode)