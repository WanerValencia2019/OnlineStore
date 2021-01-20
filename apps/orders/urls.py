from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import create

app_name = 'orders'

urlpatterns = [
    path('',login_required(create,login_url='login'),name='create'),
]
