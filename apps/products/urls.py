from django.urls import path

##Views
from .views import Home,ProductDetail,StoreView,SearchProductView

app_name = 'products'

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('store/',StoreView.as_view(),name='store'),
    path('detail/<slug:slug>',ProductDetail.as_view(), name='detail'),
    path('store/products/',SearchProductView.as_view(),name='search')
]
