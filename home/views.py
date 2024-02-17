from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def fillForm(request):
    if request.method == 'POST':
        # Handle the form submission
        entered_skills = []
        skill_counter = 1  # Start from 1 to match the initial ID
        
        while True:
            skill_name = request.POST.get(f'skill_name_{skill_counter}')
            proficiency_level = request.POST.get(f'proficiency_level_{skill_counter}')
            
            # If any input is not found, break the loop
            if not skill_name or not proficiency_level:
                break
            
            # Append the skill to the list
            entered_skills.append({'name': skill_name, 'level': proficiency_level})
            
            # Print the received data
            print("Skill Name:", skill_name)
            print("Proficiency Level:", proficiency_level)
            
            skill_counter += 1  # Increment the counter
        
        # Example: Store the data in the session for now
        request.session['entered_skills'] = entered_skills
        
        messages.success(request, 'Skills added successfully!')
        return render(request, 'index.html')  # Render the same page
    else:
        return render(request, 'mainform.html')  # Render the form page

def signup(request):
    if request.method == "POST":
        # Handle signup form submission
        username=request.POST.get('username')
        firstname=request.POST.get('firstName')
        lastname=request.POST.get('lastName')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confpassword=request.POST.get('confirmPassword')
        if len(password)<8:
            messages.error(request,'Password Length Cannot be Less than 8!')
            return redirect('/')
        elif password!=confpassword:
            messages.error(request,'Password and Confirm Password Fields do not Match!')
            return redirect('/')
        elif len(password)<8 and password!=confpassword:
            messages.error(request,'Password Length Cannot be Less than 8!')
            messages.error(request,'Password and Confirm Password Fields do not Match!')
            return redirect('/')
        elif not username.isalnum():
            messages.error(request, "Username should be in Alphabets or Numbers only!")
            return redirect('/')
        else:
            myuser=User.objects.create_user(username, email, password)
            myuser.first_name=firstname
            myuser.last_name=lastname
            myuser.save()
            messages.success(request,'Your Account has been successfully created')
            return redirect('/')
    else:
        return render(request, 'index.html')  # Render the same page

def login(request):
    if request.method == "POST":
        # Handle login form submission
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user is not None:
            auth_login(request,user)
            messages.success(request, "Successfully Logged In!")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials! Please Try Again!")
            return redirect('/')
    else:
        return render(request, 'index.html')  # Render the same page

def logout(request):
    auth_logout(request)  # Use renamed logout function
    messages.success(request, "Successfully Logged Out!")
    return redirect("/")

