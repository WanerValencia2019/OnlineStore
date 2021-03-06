
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST, require_GET

from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from threading import Thread

from apps.shortcuts import destroy_cart, destroy_order
from .decorators import validate_cart_order
from .mail import Mail
# Create your views here.
from apps.shipping_adress.models import ShippingAdress
from .models import Order
from apps.billing_profiles.models import BillingProfiles
from apps.billing_charges.models import BillingCharge

@validate_cart_order
def create(request, cart, order):
    #print(order)
    if cart.products.all().count() == 0:
        return redirect('/')

    return render(request,'orders/order.html',{'order':order})



@validate_cart_order
def adress(request, cart, order):

    if cart.products.all().count() == 0:
        return redirect('/')

    shipping_adress = order.get_or_create_shipping_adress()

    print(shipping_adress)

    return render(request,'orders/adress.html',{'shipping_adress':shipping_adress})

def select_adress(request):
    adresses = request.user.shippingadress_set.all()

    return render(request,'orders/select_adress.html', {'adresses': adresses}) 


@validate_cart_order
def stablish_adress(request, cart, order):
    adress_id = request.POST.get('id')
    shipping_adress = get_object_or_404(ShippingAdress,pk=adress_id)

    if request.user.id != shipping_adress.user.id:
        return redirect('/')
        
    order.update_shipping_adress(shipping_adress)
    return redirect(reverse_lazy('orders:adress'))


@validate_cart_order
def billing_profile(request, cart, order):
    if cart.products.all().count() == 0 or order.shipping_adress is None:
        return redirect('/')

    billing_profile = order.get_or_create_billing_profile()

    print(billing_profile)

    return render(request,'orders/billing_profile.html',{'billing_profile':billing_profile})

@validate_cart_order
def select_billing_profile(request, cart, order):
    if cart.products.all().count() == 0:
        return redirect('/')

    billing_profiles = request.user.billingprofiles_set.all()
    return render(request,'orders/select_billing_profile.html', {'billing_profiles': billing_profiles}) 


@validate_cart_order
def stablish_billing_profile(request, cart, order):
    billing_id = request.POST.get('id')
    billing_profile = get_object_or_404(BillingProfiles,pk=billing_id)

    if request.user.id != billing_profile.user.id:
        return redirect('/')
        
    order.update_billing_profile(billing_profile)
    
    return redirect(reverse_lazy('orders:billing_profile'))

@require_GET
@validate_cart_order
def confirm_order_view(request, cart, order):

    if cart.products.all().count() == 0 or order.shipping_adress is None or order.billing_profile is None:
        return redirect(reverse_lazy('carts_cart'))

    shipping_adress = order.shipping_adress
    billing_profile = order.billing_profile

    if shipping_adress is None:
        return redirect(reverse_lazy('orders:adress'))

    if billing_profile is None:
        return redirect(reverse_lazy('orders:billing_profile'))

    return render(request,'orders/confirm.html',{
        'cart':cart,
        'order':order,
        'shipping_adress':shipping_adress,
        'billing_profile':billing_profile
        })


@require_POST
@validate_cart_order
def cancel_order(request, cart, order):

    canceled = order.cancel()

    if canceled:
        destroy_order(request)
        destroy_cart(request)
        return redirect(reverse_lazy('products:store'))

    return redirect(reverse_lazy('orders:confirm'))


@require_POST
@validate_cart_order
def complete_order(request, cart, order):
    user = request.user
    if user.id != order.user.id:
        return redirect(reverse_lazy('carts:cart'))

    charge = BillingCharge.objects.create_charge(order)

    if charge:
        order.complete()
        thread = Thread(target=Mail.send_complete_order, args=(
            user, order
        ))
        thread.start()

        destroy_order(request)
        destroy_cart(request)
        messages.success(request,'Compra realizada exítosamente')
        return redirect(reverse_lazy('products:store'))

    return redirect(reverse_lazy('carts:cart'))


class ListOrders(LoginRequiredMixin, ListView):
    login_url = 'account/login'
    queryset = Order.objects.all()
    template_name = 'orders/list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = Order.objects.filter(user__id=self.request.user.id)
        return queryset

