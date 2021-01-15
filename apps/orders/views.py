from django.shortcuts import render
from apps.shortcuts import get_or_create_cart,get_or_create_order
# Create your views here.

def create(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(request,cart)
    #print(order)

    return render(request,'orders/order.html',{'order':order})

