from django.db import models

# Create your models here.
class Registration(models.Model):
    
     firstname = models.CharField(max_length=255)
     lastname = models.CharField(max_length=255)
     Date_of_birth = models.DateField()
     gender = models.CharField(max_length=10)
     country = models.CharField(max_length=255)
     state = models.CharField(max_length=255)
     town= models.CharField(max_length=255)
     zipcode = models.CharField(max_length=10)
     phone1= models.CharField(max_length=10)
     phone2= models.CharField(max_length=10)
     email = models.EmailField(max_length=255)

     def __str__(self):
        return self.firstname

   
 


class User_account(models.Model):
    firstname = models.CharField(max_length=22 )
    lastname = models.CharField(max_length=6)
    date =  models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=22)
    country = models.CharField(max_length=30)
    town = models.IntegerField()
    state = models.CharField(max_length=30)
    num1 = models.CharField(max_length=30)
    num2 = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    