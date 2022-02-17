from django.urls import path
from . import views

app_name = 'internetshop'

urlpatterns = [
    path("", views.products, name="main"),
    path("<int:pk>", views.products, name="products")
]