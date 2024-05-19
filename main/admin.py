from django.contrib import admin
from .models import UserProfile, Skill, Project, Education, Certification, Experience, TitleTags, MenuItem, ProgrammingLanguage, Framework_Tools_Category,FrameworkAndTool

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Experience)
admin.site.register(MenuItem)

admin.site.register(ProgrammingLanguage)
admin.site.register(FrameworkAndTool)
admin.site.register(Framework_Tools_Category)
# admin.site.register(TitleTags)

