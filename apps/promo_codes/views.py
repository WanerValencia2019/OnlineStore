from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_POST
from django.contrib import messages
# Create your views here.
from apps.shortcuts import get_or_create_cart
from .models import PromoCodes

@require_POST
def promoCode(request):
    code = request.POST.get('code')
    cart = get_or_create_cart(request)
    promo_code = PromoCodes.objects.validate(code)

    if promo_code is not None:
        cart.apply_code_promo(promo_code)
        messages.add_message(request,messages.SUCCESS, "El código promocional aplicado correctamente")
    else:
        messages.add_message(request,messages.ERROR, "El código promocional no es válido")

    return redirect(reverse('carts:cart'))