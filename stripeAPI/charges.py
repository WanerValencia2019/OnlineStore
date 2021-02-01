from . import stripe


def create(order):
    if order.billing_profile and order.user.customer_id:
        charge = stripe.Charge.create(
            amount = int(order.total)*100,#convertimos el dinero a centavos de dolar
            currency='USD',
            description=order.description,
            customer = order.user.customer_id,
            source = order.billing_profile.card_id,
            metadata={
                'order_id':order.id
            }
        )

        return charge

    return None
