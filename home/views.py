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

        # Define the skill keys
        skill_keys = [
            "Android", "Angular", "AWS", "Azure", "Blockchain", "Bootstrap", "C#", "C++", "Confluence", "CSS",
            "CSS3", "Data Science", "DigitalOcean", "Django", "Docker", "Ethereum", "Git", "Google Cloud Platform",
            "GraphQL", "Heroku", "HTML", "HTML5", "iOS", "Java", "JavaScript", "Jira", "Kubernetes", "LESS",
            "Machine Learning", "MERN Stack", "MongoDB", "Node.js", "PHP", "Python", "PyTorch", "React", "RESTful API",
            "Ruby", "R", "Sass", "Solidity", "Spring Framework", "SQL", "Swift", "TensorFlow", "TypeScript", "Unity",
            "Vue.js"
        ]

        # Iterate over skill keys to extract skill names and proficiency levels
        for skill_name in skill_keys:
            proficiency_level = request.POST.get(f"{skill_name}", '0')
            # Convert proficiency level to dataset format (1 for beginner, 2 for intermediate, 3 for advanced)
            proficiency_level_value = '0' if proficiency_level == '0' else '-' + proficiency_level
            user_skills.append(proficiency_level_value)

        # Append job role (Assuming job role is always sent in the form data)
        job_role = request.POST.get('job_role', '')
        user_skills.append(job_role)

        # Print the user skills list
        print("User Skills:", user_skills)
        print("Number of skills:", len(user_skills))

        # You can now use this list for further processing, such as applying k-means clustering
        messages.success(request, "Submitted Successfully")
        return render(request, 'mainform.html')
    else:
        skills = [  # List of available skills
            "Python", "Java", "JavaScript", "HTML", "CSS", "SQL", "React", "Angular", "Node.js", "MongoDB", "Git",
            "C#", "C++", "PHP", "AWS", "Docker", "Kubernetes", "Spring Framework", "TensorFlow", "PyTorch",
            "Machine Learning", "Data Science", "R", "Ruby", "Swift", "Android", "iOS", "Unity", "Blockchain",
            "Ethereum", "Solidity", "Vue.js", "TypeScript", "HTML5", "CSS3", "Bootstrap", "Sass", "LESS",
            "RESTful API", "GraphQL", "Jira", "Confluence", "Azure", "Google Cloud Platform", "Heroku",
            "DigitalOcean", "Django", "MERN Stack"
        ]
        return render(request, 'mainform.html', {'skills': skills})  # Pass skills to the template

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

