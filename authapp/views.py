from django.shortcuts import render, HttpResponsePermanentRedirect
from django.urls import reverse
from django.contrib import auth
from .forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
# Create your views here.

def login(request):
    if request.method == 'POST':
        login_form = ShopUserLoginForm(data=request.POST)

        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(request, username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponsePermanentRedirect(reverse('main'))
    else:
        login_form = ShopUserLoginForm()

    return render(request, 'login.html', context={
        'title': 'Вход',
        'form': login_form
    })

def logout(request):
    auth.logout(request)
    return HttpResponsePermanentRedirect(reverse('main'))

def register(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(data=request.POST)
        if register_form.is_valid():
            register_form.save()
            return HttpResponsePermanentRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    return render(request, 'register.html', context={
        'title': 'Регистрация',
        'form': register_form
    })

def edit(request):
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponsePermanentRedirect(reverse('main'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    return render(request, 'register.html', context={
        'title': 'Регистрация',
        'form': edit_form
    })