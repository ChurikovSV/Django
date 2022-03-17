from django.urls import path
from . import views

app_name = 'internetshop'

urlpatterns = [
    path("", views.products, name="all"),
    path("<int:category_id>", views.category, name="category"),
    path("product/<int:product_id>", views.product, name="product")
]