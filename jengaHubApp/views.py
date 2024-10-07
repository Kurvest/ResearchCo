from django.shortcuts import render
from .models import Project, Feedback

from django.shortcuts import render, get_object_or_404
from .models import Professional, Project

def professional_profile(request, professional_id):
    professional = get_object_or_404(Professional, id=professional_id)
    projects = Project.objects.filter(professional=professional)
    return render(request, 'jengaHubApp/profile.html', {'professional': professional, 'projects': projects})

def add_project(request):
    if request.method == 'POST':
        # Handle project creation form
        pass
    return render(request, 'jengaHubApp/add_project.html')
