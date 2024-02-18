# In populate_skills.py

from django.core.management.base import BaseCommand
from home.models import Skill

class Command(BaseCommand):
    help = 'Populate the database with skills'

    def handle(self, *args, **kwargs):
        skills = [
            "Android", "Angular", "AWS", "Azure", "Blockchain", "Bootstrap", "C#", "C++", "Confluence", "CSS",
            "CSS3", "Data Science", "DigitalOcean", "Django", "Docker", "Ethereum", "Git", "Google Cloud Platform",
            "GraphQL", "Heroku", "HTML", "HTML5", "iOS", "Java", "JavaScript", "Jira", "Kubernetes", "LESS",
            "Machine Learning", "MERN Stack", "MongoDB", "Node.js", "PHP", "Python", "PyTorch", "React", "RESTful API",
            "Ruby", "R", "Sass", "Solidity", "Spring Framework", "SQL", "Swift", "TensorFlow", "TypeScript", "Unity",
            "Vue.js"
        ]

        for skill_name in skills:
            skill, created = Skill.objects.get_or_create(name=skill_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Skill "{skill_name}" created successfully'))
            else:
                self.stdout.write(self.style.WARNING(f'Skill "{skill_name}" already exists'))
