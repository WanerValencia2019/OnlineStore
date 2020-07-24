from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.db.models import Q


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


class ProductDetail(DetailView):
    model = Product
    template_name= 'products/detail.html'

class SearchProductView(ListView):
    model = Product
    template_name = 'products/searchResult.html'
    context_object_name = 'products'


    def get_queryset(self):
        search = self.request.GET['search']
        queryset = Product.objects.filter(Q(title__icontains=search) | Q(category_products__title__icontains=search))
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET['search'] 
        return context
    



