
from django.shortcuts import render, get_object_or_404
from .models import Professional, Project
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful signup
            return redirect('home')  # Redirect to home page after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


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
    return render(request, 'projects.html')

# Professionals page view
def professionals(request):
    return render(request, 'professionals.html')

# Contact page view
def contact(request):
    return render(request, 'contact.html')

# Profile page view (requires login)
def profile(request):
    return render(request, 'profile.html')

# About page view
def about(request):
    return render(request, 'about.html')

# Privacy policy page view
def privacy(request):
    return render(request, 'privacy.html')

# Terms of service page view
def terms(request):
    return render(request, 'terms.html')
