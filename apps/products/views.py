from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.db.models import Q

from apps.category.models import Category
from apps.carts.models import Cart

from .models import Product
# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'products/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.all()[:10]
        return queryset
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news']=Product.objects.get_news()[:6]
        print(Product.objects.get_news())
        return context

class StoreView(ListView):
    queryset = Product.objects.all()  
    template_name = 'products/store.html'
    context_object_name = 'products'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        return  context


class ProductDetail(DetailView):
    model = Product
    template_name= 'products/detail.html'

class SearchProductView(ListView):
    model = Product
    template_name = 'products/searchResult.html'
    context_object_name = 'products'


    def get_queryset(self):
        try:
            search = self.request.GET.get('search')
            queryset = Product.objects.filter(Q(title__icontains=search) | Q(category_products__title__icontains=search))
        except Exception:
            min = self.request.GET.get('min')
            max = self.request.GET.get('max')
            queryset = Product.objects.filter(Q(price__gte=min) & Q(price__lte=max))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["query"] = self.request.GET['search']
        except: 
            pass

        context['categories'] = Category.objects.all()
        return context
    



