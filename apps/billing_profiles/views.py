from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
# Create your views here.
from django.contrib import messages
from apps.billing_profiles.models import BillingProfiles

class Create(LoginRequiredMixin,View):
	login_url='account/login'
	template_name = 'billing_profiles/create.html'

	def get(self,request,*args, **kwargs):
		stripePublicKey = settings.STRIPE_PUBLIC_KEY
		return render(request, self.template_name,{
				'stripePublicKey':stripePublicKey
			})

	def post(self,request,*args, **kwargs):
		data = request.POST
		if data['stripeToken']:
			request.user.create_customer_id()
			BillingProfiles.objects.create_by_stripe_token(request.user,data['stripeToken'])
			messages.add_message(request, messages.SUCCESS, "Tarjeta agrega correctamente")
			
		return redirect('/billing_profiles/create')