
from django.shortcuts import render, get_object_or_404
from .models import Professional, Project
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful signup
            #HttpResponseRedirect(reverse(''))
            return redirect('jengaHubApp:home')  # Redirect to home page after signup
    else:
        form = UserCreationForm()
    return render(request, 'jengaHubApp/signup.html', {'form': form})


def home(request):
    return render(request, 'jengaHubApp/home.html') 

def professional_profile(request):
    professionals = Professional.objects.all()  # Retrieve all professionals
    context = {
        'professionals': professionals
    }
    return render(request, 'jengaHubApp/profile.html', context)
    

def professional_projects(request, professional_id):
    professional = get_object_or_404(Professional, id=professional_id)
    projects = professional.projects.all() 
    #projects = Project.objects.filter(professional=professional)
    return render(request, 'jengaHubApp/projects.html', {
        'professional': professional,
        'projects': projects
    })
def project(request, profile_id):
    profile = get_object_or_404(Professional, id=profile_id)
    projects = Project.objects.filter(professional=profile)
    return render(request, 'jengaHubApp/projects.html', {'profile': profile, 'projects': projects})

def add_project(request):
    if request.method == 'POST':
        # Handle project creation form
        pass
    return render(request, 'jengaHubApp/add_project.html')


# Projects page view
def projects(request):
    return render(request, 'jengaHubApp:projects.html')

# Professionals page view
def professionals(request):
    return render(request, 'jengaHubApp:professionals.html')

# Contact page view
def contact(request):
    return render(request, 'jengahubApp:contact.html')

# Profile page view (requires login)
def profile(request):
    return render(request, 'jengaHubApp:profile.html')

# About page view
def about(request):
    return render(request, 'jengaHubApp:about.html')

# Privacy policy page view
def privacy(request):
    return render(request, 'jengaHubApp:privacy.html')

# Terms of service page view
def terms(request):
    return render(request, 'jengaHubApp:terms.html')
