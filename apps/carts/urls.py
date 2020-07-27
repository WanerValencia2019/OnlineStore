from django.urls import path


from .views import cart,  addProduct, removeProduct

app_name = 'carts'

urlpatterns = [
    path('',cart,name='cart'),
    path('add/',addProduct,name='addProduct'),
    path('remove/<int:id>',removeProduct,name='removeProduct')    
]
