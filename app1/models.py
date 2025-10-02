from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=100)
    price = models.IntegerField()
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    seat = models.IntegerField()
    transmission = models.CharField(max_length=100)
    car_img = models.ImageField(upload_to='car')
    is_published = models.BooleanField(default=False)