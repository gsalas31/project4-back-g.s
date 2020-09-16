# from django.db import models
# from apps.authentication.models import User
# #or user
#
# # Create your models here.
#
# class Comment(models.Model):
#     class Meta:
#         verbose_name_plural = 'comments'
#
#     subject = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.subject
#
#
