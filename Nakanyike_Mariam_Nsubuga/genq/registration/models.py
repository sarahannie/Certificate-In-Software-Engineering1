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
   
 