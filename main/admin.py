from django.contrib import admin
from .models import NavigationItem, Skill, Project, Certification, Resume, SocialMediaLink

admin.site.register(NavigationItem)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Certification)
admin.site.register(Resume)
admin.site.register(SocialMediaLink)
