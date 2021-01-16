from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import create, adress, select_adress, stablish_adress

app_name = 'orders'

urlpatterns = [
    path('',login_required(create,login_url='login'),name='create'),
    path('shipping_adress/',login_required(adress,login_url='login'),name='adress'),
    path('shipping_adress/select',login_required(select_adress,login_url='login'),name='select_adress'),
    path('shipping_adress/stablish',login_required(stablish_adress,login_url='login'),name='stablish_adress'),
]
