
from django.core.management.base import BaseCommand
from home.models import JobRole
class Command(BaseCommand):
    help = 'Populate job roles in the database'

    def handle(self, *args, **kwargs):
        # Define a list of job roles
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

        # Iterate over the list and create JobRole objects
        for role in job_roles:
            JobRole.objects.get_or_create(name=role)

        self.stdout.write(self.style.SUCCESS('Job roles have been successfully populated'))