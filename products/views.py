from django.shortcuts import render
from .models import Product

def get_products(request,slug):
    try:
        product= Product.objects.get(slug=slug)
        return render(request,'products/products.html',context={'product':product})
    except Exception as e:
        print(e)