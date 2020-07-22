from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'store/home.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['news']=Product.objects.get_news()
        print(Product.objects.get_news())
        return context