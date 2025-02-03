from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=5)
    contact = models.CharField(max_length=15)

class BloodStock(models.Model):
    blood_group = models.CharField(max_length=5)
    quantity = models.IntegerField()  # in units
