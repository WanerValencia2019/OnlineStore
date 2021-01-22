from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views


app_name = 'orders'

urlpatterns = [
    path('',login_required(views.create,login_url='login'),name='create'),
    path('shipping_adress/',login_required(views.adress,login_url='login'),name='adress'),
    path('shipping_adress/select',login_required(views.select_adress,login_url='login'),name='select_adress'),
    path('shipping_adress/stablish',login_required(views.stablish_adress,login_url='login'),name='stablish_adress'),
    path('confirm',login_required(views.confirm_order_view,login_url='login'),name='confirm'),
    path('cancel',login_required(views.cancel_order,login_url='login'),name='cancel'),
    path('complete',login_required(views.complete_order,login_url='login'),name='complete'),
    path('list',views.ListOrders.as_view(),name='list'),
]
