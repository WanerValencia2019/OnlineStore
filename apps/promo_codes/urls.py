from django.urls import path
from .views import promoCode

app_name = 'promo_codes'

urlpatterns = [
    path('', promoCode, name='code'),
]
