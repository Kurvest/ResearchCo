from django.urls import path
from . import views
app_name = 'jengaHubApp'

urlpatterns = [
    path('profile/<int:professional_id>/', views.professional_profile, name='professional_profile'),
    path('add_project/', views.add_project, name='add_project'),
]
