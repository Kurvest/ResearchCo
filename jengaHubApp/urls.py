from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'jengaHubApp'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('professional/<int:professional_id>/projects/', views.professional_projects, name='professional_projects'),
    path('project/', views.project, name='project'), 
    path('profile/', views.professional_profile, name='professional_profile'),
    path('add_project/', views.add_project, name='add_project'),
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('professionals/', views.professionals, name='professionals'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
]

urlpatterns += [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),  # You need to create the signup view
]

