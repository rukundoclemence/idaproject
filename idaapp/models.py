from django.db import models

# Create your models here.
class student (models.Model):
    name = models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    phone=models.CharField(max_length=25)
def __str__(self):
    return self.name