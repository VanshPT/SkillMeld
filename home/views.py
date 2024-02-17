from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def fillForm(request):
    if request.method == 'POST':
        # Handle the form submission
        user_skills = []

        # Retrieve data from the form
        job_role = request.POST.get('job_role')

        # List to store skill levels
        skill_levels = []

        # Iterate over submitted skill inputs
        for key, value in request.POST.items():
            if key.startswith('skill_name_'):
                skill_name = value
                # Extract skill level from the corresponding proficiency level field
                proficiency_level = request.POST.get('proficiency_level_' + key.split('_')[-1])
                user_skills.append({'name': skill_name, 'level': proficiency_level})

        # Process the user_skills data as needed
        # For now, just print it
        skills = [
            "Android", "Angular", "AWS", "Azure", "Blockchain", "Bootstrap", "C#", "C++", "Confluence", "CSS",
            "CSS3", "Data Science", "DigitalOcean", "Django", "Docker", "Ethereum", "Git", "Google Cloud Platform",
            "GraphQL", "Heroku", "HTML", "HTML5", "iOS", "Java", "JavaScript", "Jira", "Kubernetes", "LESS",
            "Machine Learning", "MERN Stack", "MongoDB", "Node.js", "PHP", "Python", "PyTorch", "React", "RESTful API",
            "Ruby", "R", "Sass", "Solidity", "Spring Framework", "SQL", "Swift", "TensorFlow", "TypeScript", "Unity",
            "Vue.js"
        ]

        # Check skills against user_skills
        for skill in skills:
            skill_found = False
            for skill_dict in user_skills:
                if skill_dict['name'] == skill:
                    skill_found = True
                    if 'beginner' in skill_dict['level'].lower():
                        skill_levels.append(1)
                    elif skill_dict['level'] == 'intermediate':
                        skill_levels.append(2)
                    elif skill_dict['level'] == 'advanced':
                        skill_levels.append(3)
                    break
            if not skill_found:
                skill_levels.append(0)

        # Append jobpost at the end
        skill_levels.append(job_role)

        # Print the skill levels

        # You might want to save user_skills to the database or perform some other actions here

        # Return an HttpResponse or redirect to another page
        messages.success(request, "data submitted successfully")
        return render(request, 'mainform.html')

    else:
        # If the request method is GET, render the form with skill options
        skills = [
            "Android", "Angular", "AWS", "Azure", "Blockchain", "Bootstrap", "C#", "C++", "Confluence", "CSS",
            "CSS3", "Data Science", "DigitalOcean", "Django", "Docker", "Ethereum", "Git", "Google Cloud Platform",
            "GraphQL", "Heroku", "HTML", "HTML5", "iOS", "Java", "JavaScript", "Jira", "Kubernetes", "LESS",
            "Machine Learning", "MERN Stack", "MongoDB", "Node.js", "PHP", "Python", "PyTorch", "React", "RESTful API",
            "Ruby", "R", "Sass", "Solidity", "Spring Framework", "SQL", "Swift", "TensorFlow", "TypeScript", "Unity",
            "Vue.js"
        ]
        return render(request, 'mainform.html', {'skills': skills})



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
            messages.success(request,'Your Blogme Account has been successfully created')
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

