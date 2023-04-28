from django.db import models

# Create your models here.
class User_account(models.Model):
    firstname = models.CharField(max_length=22 )
    lastname = models.CharField(max_length=6)
    date =  models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=22)
    country = models.CharField(max_length=30)
    town = models.IntegerField(max_length=20)
    state = models.CharField(max_length=30)
    num1 = models.CharField(max_length=30)
    num2 = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    
    