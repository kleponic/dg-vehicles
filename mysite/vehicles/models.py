from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Vehicle(models.Model):
    name = models.CharField(max_length=50)
    driver = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    capacity = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"

    def __str__(self):
        return self.name
    
    
		