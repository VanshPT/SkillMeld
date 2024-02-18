from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
import requests
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

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

        # List of available skills and job roles
        skills = [
            "Android", "Angular", "AWS", "Azure", "Blockchain", "Bootstrap", "C#", "C++", "Confluence", "CSS",
            "CSS3", "Data Science", "DigitalOcean", "Django", "Docker", "Ethereum", "Git", "Google Cloud Platform",
            "GraphQL", "Heroku", "HTML", "HTML5", "iOS", "Java", "JavaScript", "Jira", "Kubernetes", "LESS",
            "Machine Learning", "MERN Stack", "MongoDB", "Node.js", "PHP", "Python", "PyTorch", "React", "RESTful API",
            "Ruby", "R", "Sass", "Solidity", "Spring Framework", "SQL", "Swift", "TensorFlow", "TypeScript", "Unity",
            "Vue.js"
        ]
        job_roles = [
            'Backend Engineer', 'Technical Support Engineer', 'QA Automation Engineer', 
            'IT Support Specialist', 'Data Modeler', 'Network Administrator', 
            'UI Architect', 'Data Scientist', 'UI Developer', 'DevOps Engineer', 
            'AI Engineer', 'Product Manager', 'ETL Developer', 'Solutions Architect', 
            'Frontend Development Lead', 'Project Manager', 'Software Engineer', 
            'Backend Development Manager', 'DevOps Lead', 'Release Manager', 
            'Cloud Solutions Architect', 'Product Owner', 'UX Architect', 
            'Backend Development Lead', 'System Administrator', 'Software Developer', 
            'Cybersecurity Analyst', 'Database Administrator', 'Cybersecurity Engineer', 
            'Network Engineer', 'Frontend Developer', 'UX Designer', 
            'Product Development Manager', 'Quality Assurance Engineer', 
            'Embedded Systems Engineer', 'Backend Architect', 'Backend Developer', 
            'Django Developer', 'Computer Vision Engineer', 'Data Science Manager', 
            'Cybersecurity Lead', 'UI/UX Designer', 'Data Analyst', 'UX Lead', 
            'Business Analyst', 'Chief Technology Officer (CTO)', 'Cybersecurity Manager', 
            'QA Lead', 'Big Data Engineer', 'Data Engineer', 'Frontend Development Manager', 
            'Game Developer', 'Blockchain Developer', 'Software Development Manager', 
            'MERN Developer', 'Engineering Director', 'Cloud Engineer', 
            'AI Product Manager', 'Data Warehouse Architect', 'Frontend Engineer', 
            'Cloud Security Engineer', 'Web Developer', 'iOS Developer', 
            'UI Development Lead', 'Machine Learning Engineer', 'Android Developer', 
            'Full Stack Developer', 'Technical Writer', 'QA Manager', 'Platform Engineer', 
            'Frontend Architect', 'Data Product Manager', 'Embedded Software Engineer', 
            'SRE (Site Reliability Engineer)', 'Data Engineering Manager', 
            'AI Engineering Manager', 'Enterprise Architect', 'Network Security Engineer', 
            'Data Engineering Lead', 'Data Architect', 'IT Manager', 
            'Software Development Director', 'Machine Learning Lead', 'Software Architect', 
            'Automation Engineer', 'Cloud Architect'
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

        # Perform KMeans clustering
        file_path = r'C:\Users\Vansh\Desktop\SkillMeld\home\new_file11.csv'
        df = pd.read_csv(file_path)
        df = df.drop(columns=['Unnamed: 0'])
        filtered_df = df[df['Job_Role'] == job_role].copy()

        # Drop the 'Job_Role' column
        filtered_df.drop(columns=['Job_Role'], inplace=True)
        df = filtered_df.copy()

        # Perform KMeans clustering
        X = df.values
        ss = StandardScaler()
        Xs = ss.fit_transform(X)
        kmeans = KMeans(n_clusters=5, random_state=42)
        kmeans.fit(Xs)
        nearest_centroid_index = kmeans.predict([skill_levels])[0]
        nearest_centroid = kmeans.cluster_centers_[nearest_centroid_index]

        # Calculate the differences in skill levels between the user's submitted skills and the centroid
        skill_differences = nearest_centroid - skill_levels

        # Get the skills with positive differences
        positive_difference_skills = [skill for skill, difference in zip(skills, skill_differences) if difference > 0]

        return render(request, 'mainform.html', {'skills': skills, 'job_roles': job_roles, 'positive_difference_skills': positive_difference_skills})

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

        job_roles = [
            'Backend Engineer', 'Technical Support Engineer', 'QA Automation Engineer', 
            'IT Support Specialist', 'Data Modeler', 'Network Administrator', 
            'UI Architect', 'Data Scientist', 'UI Developer', 'DevOps Engineer', 
            'AI Engineer', 'Product Manager', 'ETL Developer', 'Solutions Architect', 
            'Frontend Development Lead', 'Project Manager', 'Software Engineer', 
            'Backend Development Manager', 'DevOps Lead', 'Release Manager', 
            'Cloud Solutions Architect', 'Product Owner', 'UX Architect', 
            'Backend Development Lead', 'System Administrator', 'Software Developer', 
            'Cybersecurity Analyst', 'Database Administrator', 'Cybersecurity Engineer', 
            'Network Engineer', 'Frontend Developer', 'UX Designer', 
            'Product Development Manager', 'Quality Assurance Engineer', 
            'Embedded Systems Engineer', 'Backend Architect', 'Backend Developer', 
            'Django Developer', 'Computer Vision Engineer', 'Data Science Manager', 
            'Cybersecurity Lead', 'UI/UX Designer', 'Data Analyst', 'UX Lead', 
            'Business Analyst', 'Chief Technology Officer (CTO)', 'Cybersecurity Manager', 
            'QA Lead', 'Big Data Engineer', 'Data Engineer', 'Frontend Development Manager', 
            'Game Developer', 'Blockchain Developer', 'Software Development Manager', 
            'MERN Developer', 'Engineering Director', 'Cloud Engineer', 
            'AI Product Manager', 'Data Warehouse Architect', 'Frontend Engineer', 
            'Cloud Security Engineer', 'Web Developer', 'iOS Developer', 
            'UI Development Lead', 'Machine Learning Engineer', 'Android Developer', 
            'Full Stack Developer', 'Technical Writer', 'QA Manager', 'Platform Engineer', 
            'Frontend Architect', 'Data Product Manager', 'Embedded Software Engineer', 
            'SRE (Site Reliability Engineer)', 'Data Engineering Manager', 
            'AI Engineering Manager', 'Enterprise Architect', 'Network Security Engineer', 
            'Data Engineering Lead', 'Data Architect', 'IT Manager', 
            'Software Development Director', 'Machine Learning Lead', 'Software Architect', 
            'Automation Engineer', 'Cloud Architect'
        ]       

        return render(request, 'mainform.html', {'skills': skills, 'job_roles': job_roles})

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

