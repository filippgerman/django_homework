from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.indexView.as_view(), name='index'),
    path('products/', views.products, name='products'),
    path('products/<int:category_id>', views.product_category, name='product_category'),
    path('contact/', views.contact, name='contact'),
]
