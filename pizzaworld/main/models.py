from django.db import models

# Create your models here.
class Contact(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    desc=models.CharField(max_length=200)
    date=models.DateField()

def __str__(self):
    return self.username
