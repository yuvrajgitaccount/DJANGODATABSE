from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    adress=models.CharField(max_length=50)
    class Meta:
        db_table ="employee"
