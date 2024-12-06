from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    email = models.EmailField()
    address =  models.TextField()


class Teacher(models.Model):
    tid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    address =  models.TextField()
    image = models.ImageField()
    salary = models.FloatField()
    subject = models.CharField(max_length=100)
    experience = models.FloatField()
    joining_date = models.DateField()
    phone = models.CharField(max_length=15)