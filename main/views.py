from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import MenuItem,Certification

# Create your views here.
def home(request):
    menu_items = MenuItem.objects.all()
    certifications = Certification.objects.all()
    return render(request,'base.html',{
        'menu_items':menu_items,
        'certifications':certifications
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

class CertificationListView(ListView):
    model = Certification
    template_name = 'base.html'  # Replace with your actual template name
    context_object_name = 'certifications'  # Optional: Specify the name of the context variable in the template

class CertificationDetailView(DetailView):
    model = Certification
    template_name = 'base.html'  # Replace with your actual template name
    context_object_name = 'certification'  # Optional: Specify the name of the context variable in the template