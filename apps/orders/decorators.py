from apps.shortcuts import get_or_create_cart,get_or_create_order

from functools import wraps

def validate_cart_order(function):
	@wraps(function)
	def wrap(request, *args,**kwargs):
		cart = get_or_create_cart(request)
		order = get_or_create_order(request, cart)
		return function(request, cart, order, *args, **kwargs)
	return wrap





	