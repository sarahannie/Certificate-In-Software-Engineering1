from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
     if request.POST =='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully')
        return redirect('register')
     else:
        form=RegistrationForm()
        context = {
        'form':form
          }
     return render(request,'register.html',context)

def new(request): 
    if request.POST =='POST':
        fname= request.POST['firstname']
        lname = request.POST['lastname']
        Dob = request.POST['Date_of_birth']
        gen = request.POST['gender']
        cou = request.POST['country']
        sta = request.POST['state']
        towns = request.POST['town']
        zipcodes = request.POST['zipcode']
        phone1s = request.POST['phone1']
        phone2s = request.POST['phone2']
        emails = request.POST['email']

        details = Registration(
            firstname = fname,
            lastname = lname,
            Date_of_birth = Dob,
            gender = gen,
            country = cou,
            state = sta,
            town = towns,
            zipcode = zipcodes,
            phone1 = phone1s,
            phone2 = phone2s,
            email = emails
        )
        details.save()
        chats = Registration.objects.all()
        print(chats)
        messages.success(request, ("Form has been submitted successfully!"))  
            

        return render(request, 'new.html')
    else:
        return render(request,'new.html')