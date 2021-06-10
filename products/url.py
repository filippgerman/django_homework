from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='index'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
]
