from django.urls import path

from .views import ProductsView

urls = [
    path("products", ProductsView.as_view(), name="list-products")
]

