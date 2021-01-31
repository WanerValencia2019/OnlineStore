from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.views.decorators.http import require_POST
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
			
		return redirect(reverse_lazy('billing_profiles:list'))

class BillingProfilesList(LoginRequiredMixin,ListView):
	login_url='account/login'
	template_name = 'billing_profiles/list.html'
	queryset = BillingProfiles.objects.all()
	context_object_name = "billing_profiles"

	def get_queryset(self):
		queryset = BillingProfiles.objects.filter(user__id=self.request.user.id)
		return queryset

@require_POST
def deleteBilling(request):
    success_url = reverse_lazy('billing_profiles:list')
    pk = request.POST.get('id')

    try:
        billing = BillingProfiles.objects.get(pk=pk).delete()
    except Exception as e:
        pass
    return redirect(success_url)

@require_POST
def defaultBilling(request):
    success_url = reverse_lazy('billing_profiles:list')
    pk = request.POST.get('id')
    try:
        billing = BillingProfiles.objects.get(pk=pk)
        billing.default = True
        billing.save()
    except Exception as e:
        pass
    return redirect(success_url)