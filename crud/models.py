from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=255)
    text=models.TextField()
    slug=models.SlugField(unique=True)
    date=models.DateField(auto_now=True)
    thumb=models.ImageField(blank=True)
    author=models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    def snippet(self):
        return self.text[:20] + '... read more'
# class Person(models.Model):
#     name=models.CharField(max_length=100)
#     last_name=models.CharField(max_length=100)
#     age=models.IntegerField()
    
#     def __str__(self):
#         return self.name