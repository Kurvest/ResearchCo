from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'jengaHubApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('professional/<int:professional_id>/projects/', views.professional_projects, name='professional_projects'),
    path('project/', views.project, name='project'), 
    path('profile/', views.professional_profile, name='professional_profile'),
    path('projects/', views.projects, name='projects'),
    path('professionals/', views.professionals, name='professionals'),
    path('contact/', views.contact, name='contact'),
    path('add-project/', views.add_project, name='add_project'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('projects/<int:professional_id>/', views.projects, name='projects'),
    path('send_message/<int:professional_id>/', views.send_message, name='send_message'),
    path('create-professional/', views.create_professional, name='create_professional'),
    path('trending-news/', views.trending_news, name='trending_news'),
    path('all_projects/', views.all_projects, name='all_projects'),
    path('professional_board', views.professional_dashboard, name='professional_dashboard'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('delete_profile/<int:professional_id>/', views.delete_profile, name='delete_profile'),


]

urlpatterns += [
    #path('login/', auth_views.LoginView.as_view(template_name='jengaHubApp/login.html'), name='login'),
    path('logout/', views.custom_logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('login/',views.login_view, name='login'), 
]

