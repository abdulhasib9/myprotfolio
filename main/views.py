from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import MenuItem,Certification,UserProfile,Experience,Education,ProgrammingLanguage,Skill,FrameworkAndTool,Project
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    menu_items = MenuItem.objects.all()
    certifications = Certification.objects.all()
    profile = UserProfile.objects.values('bio').get()
    return render(request,'main/index.html',{
        'menu_items':menu_items,
        'certifications':certifications,
        'profile':profile
    })
 
def list_project(request):
    menu_items = MenuItem.objects.all()
    projects = Project.objects.all()
    paginator = Paginator(projects, 5)  # Show 5 projects per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'menu_items':menu_items
    }
    return render(request, 'main/projects.html', context)
    
def list_experience(request):
    menu_items = MenuItem.objects.all()
    experiences  = Experience.objects.all()
    educations = Education.objects.all()
    programming_languages = ProgrammingLanguage.objects.all()
    skills = Skill.objects.all()
    framework_tools = FrameworkAndTool.objects.all()
    
    context = {
        'experiences':experiences,
        'menu_items':menu_items,
        'educations':educations,
        'programming_languages':programming_languages,
        'skills':skills,
        'framework_tools':framework_tools
        
    }
    return render(request,'main/resume.html',context)


def about(request):
    menu_items = MenuItem.objects.all()
    return render(request,'main/about.html',{
        'menu_items': menu_items
    })

def menu_item_list(request):
    menu_items = MenuItem.objects.all()
    
    return render(request, 'partials/_nav.html', {'menu_items': menu_items})



# class MenuItemListView(ListView):
#     model = MenuItem
#     template_name = 'partials/_nav.html'  # Replace 'menu_item_list.html' with your actual template name
#     context_object_name = 'menu_items'  # Optional: Specify the name of the context variable in the template

# class MenuItemDetailView(DetailView):
#     model = MenuItem
#     template_name = 'menu_item_detail.html'  # Replace 'menu_item_detail.html' with your actual template name
#     context_object_name = 'menu_item'  # Optional: Specify the name of the context variable in the template

# class CertificationListView(ListView):
#     model = Certification
#     template_name = 'main/certifications.html' 
#     # Replace with your actual template name
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
        
#         # Add data to context
#         context['certifications'] = Certification.objects.all()
#         context['menu_item'] = MenuItem.objects.all()
        
#         return context

def certifications(request):
    menu_items = MenuItem.objects.all()
    certifications = Certification.objects.all()
    profile = UserProfile.objects.values('bio').get()
    return render(request,'main/certifications.html',{
        'menu_items':menu_items,
        'certifications':certifications,
        'profile':profile
    })
      




def certification_list(request):
    certifications = Certification.objects.all()
    paginator = Paginator(certifications, 10)  # Number of items per page
    menu_items = MenuItem.objects.all()
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'menu_items':menu_items,
    }
    
    return render(request, 'main/certifications.html',context)


# class CertificationDetailView(DetailView):
#     model = Certification
#     template_name = 'base.html'  # Replace with your actual template name
#     context_object_name = 'certification'  # Optional: Specify the name of the context variable in the template