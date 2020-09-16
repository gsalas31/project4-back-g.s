from django.db import models

# Create your models here.

class Tutorial(models.Model):
    class Meta:
        verbose_name_plural = 'tutorials'

    title = models.CharField(blank=True)
    materials = models.TextField


