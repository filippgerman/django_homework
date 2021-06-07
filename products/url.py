from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.main, name='index'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
]


