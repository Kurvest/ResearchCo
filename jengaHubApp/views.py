from django.shortcuts import render
from .models import Project, Feedback

from django.shortcuts import render, get_object_or_404
from .models import Professional, Project

def home(request):
    return render(request, 'jengaHubApp/home.html') 

def professional_profile(request):
    professionals = Professional.objects.all()  # Retrieve all professionals
    context = {
        'professionals': professionals
    }
    return render(request, 'jengaHubApp/profile.html', context)
    
def project(request, profile_id):
    profile = get_object_or_404(Professional, id=profile_id)
    projects = Project.objects.filter(professional=profile)
    return render(request, 'profiles/project_list.html', {'profile': profile, 'projects': projects})

def add_project(request):
    if request.method == 'POST':
        # Handle project creation form
        pass
    return render(request, 'jengaHubApp/add_project.html')


