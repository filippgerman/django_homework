from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.template.loader import render_to_string
from django.http import JsonResponse

from basket.models import Basket
from products.models import Product


@login_required
def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user_id=request.user.pk, product_id=product).first()

    if not basket:
        basket = Basket(user_id=request.user.pk, product_id=product.pk)

    basket.quantity += 1
    basket.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    Basket.objects.get(pk=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=pk)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.filter(user_id=request.user.id)
        context = {'baskets': baskets}
        result = render_to_string('basket/basket.html', context)
        return JsonResponse({'result': result})
