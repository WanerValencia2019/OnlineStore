from django.db import models
from django.contrib.auth.models import AbstractUser
from stripeAPI import customers


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='Correo electrónico',unique=True)
    customer_id = models.CharField(max_length=100, verbose_name="Customer Stripe ID", blank=True, null=True)

    def has_customer(self):
        return self.customer_id is not None

    def create_customer_id(self):
    	if not self.has_customer():
    		customer = customers.create(self)
    		self.customer_id = customer.id
    		self.save()

    @property
    def description(self):
    	return "Descripcion del usuario "+self.get_full_name()
    @property
    def shipping_adress(self):
        return self.shippingadress_set.filter(default=True).first()

    @property
    def billing_profile(self):
        return self.billingprofiles_set.filter(default=True).first()
        
# Create your models here.
