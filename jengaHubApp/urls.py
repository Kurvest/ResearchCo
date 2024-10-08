from django.urls import path
from . import views
app_name = 'jengaHubApp'

urlpatterns = [
    path('', views.home, name='home'), 
     path('project/', views.project, name='home'), 
    path('profile/', views.professional_profile, name='professional_profile'),
    path('add_project/', views.add_project, name='add_project'),
]
