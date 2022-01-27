from django.shortcuts import render
from datetime import timedelta
from django.utils import timezone

# Create your views here.

MENU_LINKS = [
    {'url': 'main', 'name': 'домой'},
    {'url': 'products', 'name': 'продукты'},
    {'url': 'contact', 'name': 'контакты'},
]

def index(request):
    return render(request, 'index.html', context = {
        'variable': 'hello text',
        'datetime': timezone.now() + timedelta(days=1),
        'title': 'Главная',
        'menu_links': MENU_LINKS
    })

def products(request):
    return render(request, 'products.html', context = {
        'title': 'Продукты',
        'menu_links': MENU_LINKS
    })

def contact(request):
    return render(request, 'contact.html', context = {
        'title': 'Продукты',
        'menu_links': MENU_LINKS
    })