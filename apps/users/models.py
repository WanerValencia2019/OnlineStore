import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save

from stripeAPI import customers

from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import get_template
from django.conf import settings

from django_rest_passwordreset.signals import reset_password_token_created


class CustomUser(AbstractUser):
    id = models.CharField(max_length=36, primary_key=True, blank=True)
    email = models.EmailField(verbose_name='Correo electrónico', unique=True)
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
        return "Descripcion del usuario " + self.get_full_name()

    @property
    def shipping_adress(self):
        return self.shippingadress_set.filter(default=True).first()

    @property
    def billing_profile(self):
        return self.billingprofiles_set.filter(default=True).first()


@receiver(pre_save, sender=CustomUser)
def set_uuid(instance, *args, **kwargs):
    if not instance.id:
        instance.id = uuid.uuid4().hex
        print(instance.id)

#SIGNAL FOR SEND EMAIL ON RESET PASSWORD(SEND TOKEN)
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(
            instance.request.build_absolute_uri('/api/auth/passwordreset/confirm'),
            reset_password_token.key)
    }

    # render email text
    template = get_template('email/user_reset_password.html')
    html_content = template.render(context)

    print(reset_password_token)
    print(context)
    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="ChoquiStore"),
        # message:
        html_content,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email]
    )
    msg.content_subtype = "html"
    msg.send()

