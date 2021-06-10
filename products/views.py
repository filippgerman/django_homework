from django.shortcuts import render
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404
import datetime

def main(request):
    data = {
        'creator': 'German Filipp',
        'date': datetime.datetime.now()
    }
    return render(request, 'products/index.html', data)


def products(request):
    product = Product.objects.all()
    data = {'title': 'products', 'product': product}
    return render(request, 'products/products.html', data)
    

def contact(request):
    return render(request, 'products/contact.html')
