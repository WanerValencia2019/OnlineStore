from . import stripe

def create(user, token):
	card = stripe.Customer.create_source(
			user.customer_id,
			source=token
		)

	return card