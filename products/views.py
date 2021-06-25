from django.shortcuts import render
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

import datetime


class indexView (TemplateView):
    template_name = 'products/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['creator'] = "German Filipp"
        context['title'] = "index"
        return context

    
class UsersListView(ListView):
    model = Product
    template_name = 'products/products.html'
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    
def product_category(request, category_id):
    if not category_id:
        product = Product.objects.all()
    product = Product.objects.filter(category_id=category_id)
    category = ProductCategory.objects.all()
    data = {'title': 'products', 'product': product, 'category': category}
    return render(request, 'products/products.html', data)

def products(request):
    product = Product.objects.all()
    category = ProductCategory.objects.all()
    data = {'title': 'products', 'product': product, 'category': category}
    return render(request, 'products/products.html', data)
    

def contact(request):
    return render(request, 'products/contact.html')
