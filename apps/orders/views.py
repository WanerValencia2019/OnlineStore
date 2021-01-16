from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from apps.shortcuts import get_or_create_cart,get_or_create_order
# Create your views here.

from apps.shipping_adress.models import ShippingAdress
def create(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(request,cart)
    #print(order)

    return render(request,'orders/order.html',{'order':order})


def adress(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(request,cart)

    shipping_adress = order.get_or_create_shipping_adress()

    print(shipping_adress)

    return render(request,'orders/adress.html',{'shipping_adress':shipping_adress})

def select_adress(request):
    adresses = request.user.shippingadress_set.all()

    return render(request,'orders/select_adress.html', {'adresses': adresses}) 

def stablish_adress(request):
    adress_id = request.POST.get('id')
    cart = get_or_create_cart(request)
    order = get_or_create_order(request,cart)

    shipping_adress = get_object_or_404(ShippingAdress,pk=adress_id)

    if request.user.id != shipping_adress.user.id:
        return redirect('/')
        
    order.update_shipping_adress(shipping_adress)
    return redirect(reverse_lazy('orders:adress'))

def confirm_order(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(request,cart)

    shipping_adress = order.shipping_adress

    if shipping_adress is None:
        return redirect(reverse_lazy('orders:adress'))


    return render(request,'orders/confirm.html',{
        'cart':cart,
        'order':order,
        'shipping_adress':shipping_adress
        })