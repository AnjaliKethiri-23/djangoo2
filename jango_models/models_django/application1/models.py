from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=20)
    emp_salary=models.FloatField()
    emp_email=models.EmailField(unique=True)
    
class students(models.Model):
    std_name=models.CharField(max_length=10)
    std_pin=models.IntegerField(unique=True)