from django.db import models
from apps.authentication.models import UserManager

# Create your models here.

class Tutorial(models.Model):
    class Meta:
        verbose_name_plural = 'tutorials'

    title = models.CharField(blank=True)
    #not sure about this
    owner = models.ForeignKey(UserManager)
    description = models.TextField(blank=True)
    image = models.ImageField
    materials = models.TextField(blank=True)
    procedure = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    class Meta:
        verbose_name_plural = 'products'

    image = models.ImageField
    description = models.CharField(max_length=100)
    owner = models.ForeignKey(UserManager)

    def __str__(self):
        return self.image
