from django.db import models
from apps.authentication.models import User

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        verbose_name_plural = 'products'

    description = models.CharField(max_length=100)
    image = models.URLField(blank=True, max_length=300)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class Comment(models.Model):
    class Meta:
        verbose_name_plural = 'comments'

    subject = models.CharField(max_length=100)
    the_comment = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class Tutorial(models.Model):
    class Meta:
        verbose_name_plural = 'tutorials'

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True, max_length=300)
    materials = models.TextField(blank=True)
    procedure = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='tutorials', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title