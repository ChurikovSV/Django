from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings
from internetshop.models import Product

class Basket(models.Model):
    class Meta:
        unique_together = ['user', 'product']

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'