from django.db import models
from apps.authentication.models import UserManager
#or user

# Create your models here.

class Comment(models.Model):
    class Meta:
        verbose_name_plural = 'comments'

    subject = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(UserManager)

    def __str__(self):
        return self.subject


