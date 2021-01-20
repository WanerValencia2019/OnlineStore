from django.urls import path
from django.contrib.auth.decorators import login_required


from .views import create, adress, select_adress, stablish_adress, confirm_order_view, cancel_order, complete_order


app_name = 'orders'

urlpatterns = [
    path('',login_required(create,login_url='login'),name='create'),
    path('shipping_adress/',login_required(adress,login_url='login'),name='adress'),
    path('shipping_adress/select',login_required(select_adress,login_url='login'),name='select_adress'),
    path('shipping_adress/stablish',login_required(stablish_adress,login_url='login'),name='stablish_adress'),
    path('confirm',login_required(confirm_order_view,login_url='login'),name='confirm'),
    path('cancel',login_required(cancel_order,login_url='login'),name='cancel'),
    path('complete',login_required(complete_order,login_url='login'),name='complete'),

]
