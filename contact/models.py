from django.db import models

# Create your models here.
class formData(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=200)
    message=models.TextField()