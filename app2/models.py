from django.db import models

# Create your models here.


class Application(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_number = models.IntegerField()
    driver_license_number = models.CharField(max_length=20)
    pickup_location = models.CharField(max_length=20)
    drop_location = models.CharField(max_length=20)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    return_date = models.DateField()
    return_time = models.TimeField()

