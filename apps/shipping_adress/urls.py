from django.urls import path
from .views import Home, Create, defaultAdress, Edit, deleteAdress

app_name = 'shipping_adress'

urlpatterns = [
    path('',Home.as_view(),name='list'),
    path('create',Create.as_view(),name='create'),
    path('default',defaultAdress,name='default'),
    path('edit/<int:pk>',Edit.as_view(),name='edit'),
    path('delete',deleteAdress,name='delete'),
]
