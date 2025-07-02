from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('published', 'Published'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    tag = models.ForeignKey('Tag', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name