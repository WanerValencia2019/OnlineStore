from django.urls import path

##Views
from .views import Home,ProductDetail

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('detail/<slug:slug>',ProductDetail.as_view(), name='detail'),
]
