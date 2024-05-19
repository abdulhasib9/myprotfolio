from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True,blank=True)
    #profile_picture = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='static/profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True)
    resume = models.FileField(upload_to='static/resumes/', blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    # social_media_links = models.URLField(blank=True)
    
    def __str__(self):
        return self.email
    

class Skill(models.Model):
    LEVEL_CHOICES = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    image = models.ImageField(upload_to='skills/', blank=True)

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('software', 'Software'),
        ('network', 'Network'),
        ('cybersecurity', 'Cybersecurity'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    image = models.ImageField(upload_to='projects/')
    url = models.URLField()
    github_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES,default='software')
    

class Education(models.Model):
    title = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='education/')

def certification_image_upload_to(instance, filename):
    # Get the extension of the file
    ext = filename.split('.')[-1]
    
    # Define the new filename
    new_filename = f'{instance.title}_{timezone.now().strftime("%Y%m%d%H%M%S")}.{ext}'
    
    # Return the complete file path
    return os.path.join('static', 'certifications', new_filename)



class Certification(models.Model):
    TYPE_CHOICES = (
        ('Education', 'Education'),
        ('Career', 'Career'),
        ('Simple', 'Simple'),
    )
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    image = models.ImageField(upload_to=certification_image_upload_to)
    issue_date = models.DateField(default=timezone.now)
    validity_date = models.DateField(null=True, blank=True)
    does_not_expire = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.does_not_expire:
            self.validity_date = None
        super(Certification, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Experience(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)

    def duration(self):
        if self.end_date:
            return self.end_date - self.start_date
        else:
            return None

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class SocialMedia(models.Model):
    platform = models.CharField(max_length=255)
    url = models.URLField()
    icon = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_media')

    def __str__(self):
        return self.platform
    
class TitleTags(models.Model):
    title = models.CharField(max_length=255)
    index = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.title
    
    