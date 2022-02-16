import json

from django.shortcuts import render
from datetime import timedelta
from django.utils import timezone
from .models import Product, ProductCategory


# Create your views here.

MENU_LINKS = [
    {'url': 'main', 'name': 'домой'},
    {'url': 'products', 'name': 'продукты'},
    {'url': 'contact', 'name': 'контакты'},
]

def index(request):
    products = Product.objects.all()[:4]
    return render(request, 'index.html', context = {
        'variable': 'hello text',
        'datetime': timezone.now() + timedelta(days=1),
        'title': 'Главная',
        'menu_links': MENU_LINKS,
        'products': products
    })

def products(request):
    categories = ProductCategory.objects.all()
    return render(
        request, 'products.html',
        context = {
        'title': 'Продукты',
        'products': [],
        'menu_links': MENU_LINKS,
        'categories': categories,
    })

def contact(request):
    return render(request, 'contact.html', context = {
        'title': 'Контакты',
        'menu_links': MENU_LINKS
    })