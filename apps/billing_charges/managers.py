from django.db import models
from stripeAPI.charges import create

class BillingChargeManager(models.Manager):
    def create_charge(self, order):
            charge = create(order)

            return self.create(
                user=order.user,
                order = order,
                charge_id = charge.id,
                amount = charge.amount,
                payment_method = charge.payment_method,
                status = charge.status
            )