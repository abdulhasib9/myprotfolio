from django.urls import path
from .views import home,menu_item_list,about,certifications,certification_list,list_experience,list_project
app_name = 'main'
urlpatterns = [
    path('',home,name='home'),
    path('menu/', menu_item_list, name='menu_item_list'),
    path('about/',about,name='about'),
    path('certification/',certifications,name='certs'),
    path('certifications/', certification_list, name='certification-list'),
    path('experience/',list_experience,name='experience'),
    path('projects/',list_project,name='projects')
    # path('menu/', MenuItemListView.as_view(), name='menu_item_list'),
    # path('menu/<int:pk>/', MenuItemDetailView.as_view(), name='menu_item_detail'),
    # Other URL patterns
    #path('certifications/', CertificationListView.as_view(), name='certification_list'),
    #path('certifications/<int:pk>/', CertificationDetailView.as_view(), name='certification_detail'),
]
