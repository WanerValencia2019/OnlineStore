from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


class Mail():
    @staticmethod
    def send_complete_order(user, order):
        subject = 'Tu pedido ha sido enviado '+user.username
        template = get_template('orders/mail.html')
        content = template.render({
            'user':user,
            'order':order
        })

        message = EmailMultiAlternatives(subject, content,settings.EMAIL_HOST_USER, to=[user.email])
        message.content_subtype="html"
        message.send()

