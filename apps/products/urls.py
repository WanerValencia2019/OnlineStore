from django.urls import path

##Views
from .views import Home

urlpatterns = [
    path('',Home.as_view(),name='home')
]
