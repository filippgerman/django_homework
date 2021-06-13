from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from basket.models import Basket
from products.models import Product

@login_required
def basket(request):
    baskets = Basket.objects.filter(user_id=request.user)
    content={'title':'корзина', 'baskets':baskets}
    return render(request, 'basket/basket.html', content)


@login_required
def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user_id=request.user, product_id=product).first()

    if not basket:
        basket = Basket(user_id=request.user, product_id=product)

    basket.quantity += 1
    basket.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    Basket.objects.get(id=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
