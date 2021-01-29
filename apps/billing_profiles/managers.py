from django.db import models
from stripeAPI import cards

class BillingProfilesManager(models.Manager):
	def create_by_stripe_token(self,user, stripe_token):
		if user.has_customer() and stripe_token:
			card = cards.create(user, stripe_token)

			billing = self.create(user=user, card_id=card.id,token=stripe_token, last4 = card.last4, brand=card.brand)

			return billing
