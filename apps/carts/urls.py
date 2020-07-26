from django.urls import path


from .views import cart

app_name = 'carts'

urlpatterns = [
    path('',cart,name='cart'),    
]
