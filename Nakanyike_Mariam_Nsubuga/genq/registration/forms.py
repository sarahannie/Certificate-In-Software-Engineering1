from django import forms
from django.forms import ModelForm
#from  formValidationApp.models import *
#from validation.models import Registration
from .models import *



class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        #displaying fields
        fields = '__all__'

        #method for cleaning data
        def cleans(self):
            firstname = self.cleaned_data.get('firstname')
            lastname = self.cleaned_data.get('lastname')
            Date_of_birth = self.cleaned_data.get('Date_of_birth')
            gender = self.cleaned_data.get('gender')
            country= self.cleaned_data.get(' country')
            state = self.cleaned_data.get('state')
            town = self.cleaned_data.get('town')
            zipcode = self.cleaned_data.get('zipcode')
            phone1= self.cleaned_data.get('phone1')
            phone2= self.cleaned_data.get('phone2')
            email = self.cleaned_data.get('email')
          


            #validating 
            if len(firstname) < 2:
                self._errors['lastname'] = self.error_class(['A minimum of 2 characters is required'])
            if len(lastname) < 2:
                self._errors['lastname'] = self.error_class(['A minimum of 2 characters is required'])
            if len(town) <2 and len(state)<2 and len(country)<2 :
                self._errors['town'] = self.error_class(['A minimum of 2 characters is required'])
            return self.cleaned_data

    

    