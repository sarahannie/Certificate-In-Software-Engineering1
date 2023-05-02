from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request,'products/index.html',)

def index(request):
    return render(request, 'products/index.html')

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
