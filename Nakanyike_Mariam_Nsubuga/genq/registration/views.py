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
    
def reg(request):
       
        if request.method == "POST":
            form = RegistrationForm(request.POST or None)
            if form.is_valid():
                form.save()
                messages.success(request, ("your form has been submitted successfully."))
                return redirect('home')
                
            else:
                messages.success(request, "there was an error in your submission.")
                return render(request,'index.html')
            
            #always remember to redirect to a view that handles the page and not the page
        else:
            return render(request, 'index.html', {'form':form})
        
def aboutForm(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        date = request.POST.get('date')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        town = request.POST.get('town')
        state = request.POST.get('state')
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        email = request.POST.get('email')
       

        # Perform any processing or validation on the form data
        # ... (you can store the data in a database, send an email, etc.)

        # Redirect to a new template displaying the data as variables
        #return redirect('display', name=name, email=email, age=age, nickname=nickname, color=color)
        return redirect('display', firstname=firstname, lastname=lastname, gender=gender, country=country, town=town, state=state, num1=num1, num2=num2,  email=email, date=date)
    else:
        # Render the form template for GET request
        return render(request, 'myForm.html')

def display(request, name, email, age, nickname, color, status, hobby):
    # Process the form data and display it in a template
    context = {
        'name': name,
        'email': email,
        'age': age,
        'nickname': nickname,
        'color': color,
        'status':status,
        'hobby':hobby,
    }
    
    return render(request, 'display.html', context)