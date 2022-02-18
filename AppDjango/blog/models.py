from django.db import models

# Create your models here.
class General(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo/')
    description = models.TextField()
    
    def __str__(self):
        return self.name

# Users
class User(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    email = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name

# Posts
class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    slug = models.CharField(max_length=100, null=False)
    img = models.CharField(max_length=60)
    content = models.TextField(null=False)
    published = models.BooleanField(False)
    outstanding = models.BooleanField(False)
    creation_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title

# Categories
class Categories(models.Model):
    name = models.CharField(max_length=200, null=False)
    slug = models.CharField(max_length=100, null=False)

# Tags
class Tag(models.Model):
    name = models.CharField(max_length=200, null=False)
    slug = models.CharField(max_length=100, null=False)
    description = models.TextField()