from django.contrib import admin
from django.core.validators import MinValueValidator
from django.db import models
from unicodedata import category

from todoApp_django_RESTfulAPI import settings


class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='categories')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT, related_name='tasks')
