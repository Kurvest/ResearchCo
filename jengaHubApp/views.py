
from django.shortcuts import render, get_object_or_404
from .models import Professional, Project
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ProfessionalForm, UserSignUpForm
def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            #Professional.objects.create(user=user)
            login(request, user)  # Log the user in after successful signup
            #HttpResponseRedirect(reverse(''))
            
            messages.success(request, 'Your account has been created successfully!') 
            return redirect(reverse('jengaHubApp:create_professional'))
    else:
        form = UserSignUpForm()
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
def projects(request, professional_id):
    # Get the professional by their id
    professional = get_object_or_404(Professional, id=professional_id)

    # Get all projects related to that professional
    projects = Project.objects.filter(professional=professional)

    # Pass the professional and their projects to the template
    return render(request, 'jengaHubApp/projects.html', {
        'professional': professional,
        'projects': projects
    })

def send_message(request, professional_id):
    if request.method == 'POST':
        # Retrieve the profile of the professional
        profile = get_object_or_404(Professional, id=professional_id)
        
        # Get the message from the POST data
        message = request.POST.get('message', '').strip()  # Strip whitespace
        
        # Check if the message is not empty
        if not message:
            messages.error(request, 'Message cannot be empty.')
            return redirect('jengaHubApp:projects')  # Redirect back to the profile list
        
        try:
            # Send the email
            send_mail(
                subject=f'New Message from {request.user.username}',
                message=message,
                from_email=request.user.email,
                recipient_list=[profile.user.email],
                fail_silently=False,  # Set to False to raise an error if sending fails
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            # Log the error or handle it as needed
            messages.error(request, f'An error occurred while sending your message: {e}')
        
        return redirect('jengaHubApp:projects')

    # Optionally, handle GET requests or other methods
    messages.error(request, 'Invalid request method.')
    return redirect('jengaHubApp:professionals')

# Professionals page view
def professionals(request):
    all_professionals = Professional.objects.all()
    
    context = {
        'professionals': all_professionals
    }
    
    return render(request, 'jengaHubApp/professionals.html', context)

# Contact page view
def contact(request):
    return render(request, 'jengahubApp/contact.html')

# Profile page view (requires login)
def profile(request):
    return render(request, 'jengaHubApp/profile.html')

# About page view
def about(request):
    return render(request, 'jengaHubApp/about.html')

# Privacy policy page view
def privacy(request):
    return render(request, 'jengaHubApp/privacy.html')

# Terms of service page view
def terms(request):
    return render(request, 'jengaHubApp/terms.html')

# views.py

def create_professional(request):
    # Check if the current user already has a Professional profile
    try:
        professional = Professional.objects.get(user=request.user)
        if request.method == 'POST':
            form = ProfessionalForm(request.POST, request.FILES, instance=professional)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your professional profile has been updated successfully!')
                return redirect('jengaHubApp:professionals')  # Redirect to a profile list or any desired page
        else:
            form = ProfessionalForm(instance=professional)
    except Professional.DoesNotExist:
        # If no profile exists, create a new one
        if request.method == 'POST':
            form = ProfessionalForm(request.POST, request.FILES)
            if form.is_valid():
                professional = form.save(commit=False)
                professional.user = request.user  # Associate the professional profile with the logged-in user
                professional.save()
                messages.success(request, 'Your professional profile has been created successfully!')
                return redirect('jengaHubApp:professionals')
        else:
            form = ProfessionalForm()

    return render(request, 'jengaHubApp/create_professional.html', {'form': form})