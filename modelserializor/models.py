from django.db import models

# Create your models here.


# Create your models here.
 
class Student_Table(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=100)
