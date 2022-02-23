import json

from django.shortcuts import render, get_object_or_404
from datetime import timedelta
from django.utils import timezone
from .models import Product, ProductCategory


# Create your views here.

MENU_LINKS = [
    {'url': 'main', 'active':["main"], 'name': 'домой'},
    {'url': 'products:all', 'active':["products:all", "products"], 'name': 'продукты'},
    {'url': 'contact', 'active':["contact"], 'name': 'контакты'},
]

def index(request):
    products = Product.objects.all()[:4]
    return render(
        request,
        'index.html',
        context = {
        'variable': 'hello text',
        'datetime': timezone.now() + timedelta(days=1),
        'title': 'Главная',
        'menu_links': MENU_LINKS,
        'products': products
    })

def products(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()[:4]
    return render(
        request, 'products.html',
        context = {
        'title': 'Продукты',
        'products': products,
        'menu_links': MENU_LINKS,
        'categories': categories,
    })

def category(request, pk):
    categories = ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, id=pk)
    products = Product.objects.filter(category=category)
    return render(
        request, 'products.html',
        context = {
        'title': 'Продукты',
        'products': products,
        'menu_links': MENU_LINKS,
        'categories': categories,
        },
    )

def contact(request):
    return render(request, 'contact.html', context = {
        'title': 'Контакты',
        'menu_links': MENU_LINKS
    })
