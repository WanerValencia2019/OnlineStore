from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView,UpdateView
from django.views import View 
from django.views.decorators.http import require_POST
from .models import ShippingAdress
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
# Create your views here.

class Home(LoginRequiredMixin, ListView):
    login_url = '/account/login/'
    template_name='shipping_adress/list.html'
    context_object_name = 'shipping_adress'
    model =ShippingAdress
    queryset = ShippingAdress.objects.all().order_by('-default')

    def get_queryset(self):
        queryset = ShippingAdress.objects.filter(user__id=self.request.user.id).order_by('-default')
        return queryset



class Create(FormView):
    form_class = forms.ShippingAdressForm
    success_url = '/shipping_adress'
    template_name = 'shipping_adress/create.html'

    def get(self,request,*args, **kwargs):
        form=self.get_form_class()(initial={'user':request.user.id})
        return render(request,self.get_template_names(),{'form':form})

    
    def post(self,request,*args, **kwargs):
        form=self.get_form_class()(request.POST) 

        if form.is_valid():
            if request.GET.get('next'):
                if request.GET.get('next') == reverse_lazy('orders:adress'):
                    adress=form.save(commit=False)
                    adress.default = True
                    adress.save()
                    return redirect(request.GET.get('next'))
            form.save()
            return redirect(self.get_success_url())
        return super().get(request,args,kwargs)

class Edit(UpdateView):
    queryset = ShippingAdress.objects.all()
    form_class = forms.ShippingAdressForm
    success_url = '/shipping_adress'
    template_name = 'shipping_adress/edit.html'

    def get_object(self):
        queryset = ShippingAdress.objects.get(pk = self.kwargs.get('pk'))
        return queryset

    def get(self,request,*args, **kwargs):
        form=self.get_form_class()(instance=self.get_object())
        return render(request,self.get_template_names(),{'form':form})
    
    def post(self,request,*args, **kwargs):
        form=self.get_form_class()(request.POST, instance=self.get_object()) 
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return super().get(request,args,kwargs)

@require_POST
def deleteAdress(request):
    success_url = '/shipping_adress'
    pk = request.POST.get('id')

    try:
        adress =ShippingAdress.objects.get(pk=pk).delete()
    except e:
        pass
    return redirect(success_url)

@require_POST
def defaultAdress(request):
    success_url = '/shipping_adress'
    pk = request.POST.get('id')
    try:
        adress =ShippingAdress.objects.get(pk=pk)
        adress.default = True
        adress.save()
    except e:
        pass
    return redirect(success_url)




