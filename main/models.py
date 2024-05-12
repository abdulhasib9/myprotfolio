from django.db import models
from django.contrib.auth.models import User

class NavigationItem(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class SkillLevel(models.Model):
    LEVEL_CHOICES = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
    )
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='Beginner')

    def __str__(self):
        return self.level

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    technologies_used = models.CharField(max_length=255)
    github_link = models.URLField()
    demo_link = models.URLField(blank=True)
    skills = models.ManyToManyField(Skill, related_name='projects', blank=True)

    def __str__(self):
        return self.title

class Certification(models.Model):
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    date_earned = models.DateField()
    certificate_image = models.ImageField(upload_to='certificates/', null=True, blank=True)
    certificate_link = models.URLField(blank=True)
    projects = models.ManyToManyField(Project, related_name='certifications', blank=True)

    def __str__(self):
        return self.title

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    file_path = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.title

class SocialMediaLink(models.Model):
    platform = models.CharField(max_length=255)
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.platform} - {self.user.username}"
