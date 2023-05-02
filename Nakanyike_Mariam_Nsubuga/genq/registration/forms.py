from django import forms
from django.forms import ModelForm
#from  formValidationApp.models import *
#from validation.models import Registration
from .models import *



class RegistrationForm(ModelForm):
     class Meta:
        model = Registration
        fields = ['firstname', 'lastname', 'Date_of_birth',
                   'gender', 'country', 'state',
                     'town', 'zipcode', 'phone1', 'phone2',
                       'email']


       