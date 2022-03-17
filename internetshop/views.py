import json
import random

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

def get_hot_product():
    return random.choice(Product.objects.all())

def products(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    hot_product = get_hot_product(products)
    return render(
        request, 'products.html',
        context = {
        'title': 'Продукты',
        'hot_product': hot_product,
        'products': products.exclude(pk=hot_product.pk)[:4],
        'menu_links': MENU_LINKS,
        'categories': categories,
    }
    )

def category(request, pk):
    categories = ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, id=category_id)
    products = Product.objects.filter(category=category)
    hot_product = get_hot_product(products)
    return render(
        request, 'products.html',
        context = {
        'title': 'Продукты',
        'hot_product': get_hot_product(products),
        'products': products.exclude(pk=hot_product.pk)[:4],
        'catrgory': category,
        'menu_links': MENU_LINKS,
        'categories': categories,
        },
    )
def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = ProductCategory.objects.all()
    return render(
        request, 'product.html',
        context = {
        'title': 'Продукты',
        'product': product,
        'menu_links': MENU_LINKS,
        'categories': categories,
    }
    )

def contact(request):
    return render(request, 'contact.html', context = {
        'title': 'Контакты',
        'menu_links': MENU_LINKS
    })
