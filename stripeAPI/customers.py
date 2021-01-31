from . import stripe


def create(user):
	customer = stripe.Customer.create(
		description=user.description,
		email=user.email,
		name=user.get_full_name()
	)

	print(customer)

	return customer


