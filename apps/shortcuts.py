from apps.carts.models import Cart
from apps.orders.models import Order

from django.db import IntegrityError

def get_or_create_cart(request):
    cart_id = request.session.get('cart_id') 
    user = request.user if request.user.is_authenticated else None

    try:
        cart = Cart.objects.get(cart_id=cart_id)
    except Cart.DoesNotExist:
        cart =  Cart.objects.create(user=user)            
        
    request.session['cart_id'] = cart.cart_id

    if  user is not None and cart.user is None:
        cart.user = user
        cart.save()

    return cart

def get_or_create_order(request,cart):
    order_id = request.session.get('order_id') 
    #cart_id = Cart.objects.get(cart_id=request.session.get('cart_id'))
    user = request.user 
    order = cart.order

    if order is None and user.is_authenticated:
        order =  Order.objects.create(user=user,cart=cart)                

    request.session['order_id'] = order.order_id

    return order
    

