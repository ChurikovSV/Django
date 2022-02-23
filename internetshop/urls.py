from django.urls import path
from . import views

app_name = 'internetshop'

urlpatterns = [
    path("", views.products, name="all"),
    path("<int:pk>", views.category, name="category")
]