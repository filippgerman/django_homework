from django.shortcuts import render

def main(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')


def contact(request):
    return render(request, 'products/contact.html')
