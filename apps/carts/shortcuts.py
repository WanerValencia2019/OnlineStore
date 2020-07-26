from .models import Cart
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