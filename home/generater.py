import random
import csv

# Define the job roles
job_roles = [
    "Android Developer", "Angular Developer", "AWS Cloud Engineer", "Azure Solutions Architect", 
    "Blockchain Developer", "C# Developer", "C++ Developer", "Confluence Administrator", 
    "CSS Developer", "Data Scientist", "Django Developer", "Docker Engineer", "Ethereum Developer", 
    "Frontend Developer", "Full Stack Developer", "Git Administrator", "Google Cloud Platform Engineer", 
    "JavaScript Developer", "Java Developer", "Kubernetes Engineer", "Machine Learning Engineer", 
    "MongoDB Developer", "Node.js Developer", "PHP Developer", "Python Developer", "React Developer", 
    "Ruby on Rails Developer", "Sass Developer", "Solidity Developer", "SQL Database Administrator", 
    "Swift Developer", "TensorFlow Developer", "Unity Developer", "Vue.js Developer", "Web Developer"
]

# Define the skills and their proficiency levels for each job role
job_role_skills = {
    "Android Developer": {"Android": 3, "Java": 2, "Kotlin": 2, "RESTful API": 2},
    "Angular Developer": {"Angular": 3, "TypeScript": 3, "HTML": 2, "CSS": 2, "JavaScript": 3, "RESTful API": 2},
    "AWS Cloud Engineer": {"AWS": 3, "CloudFormation": 2, "Lambda": 2, "EC2": 2, "S3": 2, "VPC": 2},
    "Azure Solutions Architect": {"Azure": 3, "RESTful API": 3, "Azure Functions": 3, "Azure VMs": 3},
    "Blockchain Developer": {"Blockchain": 3, "Solidity": 3, "Ethereum": 3, "Smart Contracts": 3},
    "C# Developer": {"C#": 3, ".NET": 3, "ASP.NET": 3, "MVC": 3},
    "C++ Developer": {"C++": 3, "STL": 3, "Object-Oriented Programming": 3},
    "Confluence Administrator": {"Confluence": 3},
    "CSS Developer": {"CSS": 3, "SCSS": 3, "Flexbox": 3, "Grid Layout": 3},
    "Data Scientist": {"Python": 3, "R": 3, "Machine Learning": 3, "Statistics": 3, "SQL": 3},
    "Django Developer": {"Python": 3, "Django": 3, "RESTful API": 3},
    "Docker Engineer": {"Docker": 3, "Docker Compose": 3, "Containerization": 3},
    "Ethereum Developer": {"Ethereum": 3, "Solidity": 3, "Smart Contracts": 3},
    "Frontend Developer": {"HTML": 3, "CSS": 3, "JavaScript": 3, "React": 3, "Vue.js": 3, "Angular": 3},
    "Full Stack Developer": {"HTML": 3, "CSS": 3, "JavaScript": 3, "Node.js": 3, "MongoDB": 3},
    "Git Administrator": {"Git": 3, "GitHub": 3, "GitLab": 3},
    "Google Cloud Platform Engineer": {"Google Cloud Platform": 3, "Compute Engine": 3, "App Engine": 3},
    "JavaScript Developer": {"JavaScript": 3, "React": 3, "Angular": 3, "Node.js": 3},
    "Java Developer": {"Java": 3, "Spring Boot": 3, "Hibernate": 3, "RESTful Web Services": 3},
    "Kubernetes Engineer": {"Kubernetes": 3, "Docker": 3, "Microservices Architecture": 3},
    "Machine Learning Engineer": {"Python": 3, "Machine Learning": 3, "Deep Learning": 3, "TensorFlow": 3},
    "MongoDB Developer": {"MongoDB": 3, "NoSQL": 3, "MongoDB Atlas": 3},
    "Node.js Developer": {"Node.js": 3, "Express.js": 3, "RESTful API": 3},
    "PHP Developer": {"PHP": 3, "MySQL": 3, "MVC": 3},
    "Python Developer": {"Python": 3, "Django": 3, "Flask": 3, "RESTful API": 3},
    "React Developer": {"React": 3, "Redux": 3, "React Router": 3},
    "Ruby on Rails Developer": {"Ruby": 3, "Ruby on Rails": 3, "RSpec": 3},
    "Sass Developer": {"CSS": 3, "SCSS": 3, "Sass": 3},
    "Solidity Developer": {"Solidity": 3, "Ethereum": 3, "Smart Contracts": 3},
    "SQL Database Administrator": {"SQL": 3, "Database Management": 3},
    "Swift Developer": {"Swift": 3, "iOS Development": 3},
    "TensorFlow Developer": {"Python": 3, "Machine Learning": 3, "Deep Learning": 3},
    "Unity Developer": {"C#": 3, "Unity": 3, "Game Development": 3},
    "Vue.js Developer": {"Vue.js": 3, "JavaScript": 3, "HTML": 3, "CSS": 3},
    "Web Developer": {"HTML": 3, "CSS": 3, "JavaScript": 3, "React": 3, "Vue.js": 3, "Node.js": 3}
}
# Generate the dataset
data = []
for _ in range(40):  # Generate around 40 instances for each job role
    for role in job_roles:
        row = [0] * len(job_roles)
        row[job_roles.index(role)] = 1  # Set proficiency level to 1 for the respective job role
        selected_skills = random.sample(list(job_role_skills[role].keys()), random.randint(1, min(10, len(job_role_skills[role]))))

        for skill in selected_skills:
            proficiency = random.randint(1, 3)
            index = job_roles.index(role)
            row[index] = proficiency
        row.append(role)
        data.append(row)

# Write the dataset to a CSV file
with open('vansh.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(job_roles + ['Jobrole'])
    writer.writerows(data)

print("Dataset generated and saved as 'vansh.csv'.")
