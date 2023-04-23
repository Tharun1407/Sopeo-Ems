from django.db import models

# Create your models here.
class Employees(models.Model):
    Name = models.CharField(max_length=200)
    DOB = models.DateField()
    DOJ = models.DateField()
    Department = models.CharField(max_length=200)
    Post = models.CharField(max_length=200)
    Address = models.TextField()
    City = models.CharField(max_length=200)
    Country = models.CharField(max_length=200)
    Zipcode = models.IntegerField()
    State = models.CharField(max_length=200)
    Active = models.BooleanField(default=False)