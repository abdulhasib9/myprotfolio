from django.contrib import admin
from .models import UserProfile, Skill, Project, Education, Certification, Experience, TitleTags, MenuItem

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Experience)
admin.site.register(MenuItem)
# admin.site.register(TitleTags)

