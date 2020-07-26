from django.shortcuts import render


from .shortcuts import get_or_create_cart
# Create your views here.
def cart(request):
    cart = get_or_create_cart(request)

    return render(request,'carts/cart.html',{'cart':cart})
