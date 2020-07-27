from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from apps.products.models import Product
from .shortcuts import get_or_create_cart
# Create your views here.
def cart(request):
    cart = get_or_create_cart(request)
    #print(dir(cart.select_related))
    return render(request,'carts/cart.html',{'cart':cart})


def addProduct(request):
    id_product = request.POST.get('id')
    quantity = request.POST.get('quantity',1)
    cart = get_or_create_cart(request)

    product = get_object_or_404(Product,pk=id_product)

    cart.products.add(product,through_defaults={
         'quantity':quantity
    })
    messages.success(request,'Producto agregado satisfactoriamente')

    return render(request,'carts/addProduct.html',{'product':product})

def removeProduct(request,id):
    id_product = id
    print(id_product)
    cart = get_or_create_cart(request)

    product = get_object_or_404(Product,pk=id_product)
    cart.products.remove(product)
    messages.info(request,f'{product.title} eliminado satisfactoriamente')
 
    return redirect('carts:cart')