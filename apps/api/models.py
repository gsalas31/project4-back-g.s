from django.db import models
from apps.authentication.models import User

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name_plural = 'products'

    image = models.ImageField(blank=True)
    description = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image

#
# class Tutorial(models.Model):
#     class Meta:
#         verbose_name_plural = 'tutorials'
#
#     title = models.CharField(max_length=255)
#     #not sure about this
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     description = models.TextField(blank=True)
#     image = models.ImageField(blank=True)
#     materials = models.TextField(blank=True)
#     procedure = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title