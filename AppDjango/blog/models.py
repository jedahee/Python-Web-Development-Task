from django.db import models

# Create your models here.
class General(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo/')
    description = models.TextField()
    
    def __str__(self):
        return self.name