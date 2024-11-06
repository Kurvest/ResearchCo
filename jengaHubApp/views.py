
from django.shortcuts import render, get_object_or_404
from .models import Professional, Project, News
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ProfessionalForm, ProjectForm,UserSignUpForm, EmailForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Advertisement, RentalListing  # Assuming models are defined


# Optional: login form if you're not using Django's built-in views
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('jengaHubApp:professional_dashboard')
    else:
        form = AuthenticationForm()
    
    return render(request, 'jengaHubApp/login.html', {'form': form})

def profile(request):
    user_projects = Project.objects.filter(professional__user=request.user)
    context = {
        'user': request.user,
        'user_projects': user_projects,
    }
    return render(request, 'jengaHubApp/profile.html', context)


@login_required
def professional_dashboard(request):
    try:
        professional = Professional.objects.get(user=request.user)
    except Professional.DoesNotExist:
        messages.error(request, "You do not have a professional profile yet.")
        return redirect('jengaHubApp:create_professional') 
    #professional = Professional.objects.get(user=request.user)
    user_projects = Project.objects.filter(professional=professional)
    other_professionals = Professional.objects.exclude(id=professional.id)

    context = {
        'professional': professional,
        'user_projects': user_projects,
        'other_professionals': other_professionals,
    }
    return render(request, 'jengaHubApp/professional_dashboard.html', context)
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

@login_required
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
@login_required
def profile(request):
    user_projects = Project.objects.filter(professional__user=request.user)
    context = {
        'user': request.user,
        'user_projects': user_projects,
    }
    return render(request, 'jengaHubApp/profile.html', context)


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
                return redirect('jengaHubApp:professional_dashboard')  # Redirect to a profile list or any desired page
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
                return redirect('jengaHubApp:add_project')
        else:
            form = ProfessionalForm()

    return render(request, 'jengaHubApp/create_professional.html', {'form': form})

def add_project(request):
    # Check if the user has a professional profile
    professional = get_object_or_404(Professional, user=request.user)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.professional = professional
            project.save()
            messages.success(request, 'Project added successfully!')
            return redirect('jengaHubApp:professional_dashboard')
    else:
        form = ProjectForm()

    return render(request, 'jengaHubApp/add_project.html', {'form': form})

def view_projects(request, professional_id):
    professional = get_object_or_404(Professional, id=professional_id)
    projects = professional.projects.all()  # Fetch all projects for the professional
    return render(request, 'jengaHubApp/projects.html', {'professional': professional, 'projects': projects})

def trending_news(request):
    # Option 1: Fetch news from the database (for locally stored news)
    news_list = News.objects.all().order_by('-published_at')[:10]
    return render(request, 'jengaHubApp/trending_news.html', {'news_list': news_list})

def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'jengaHubApp/all_projects.html', {'projects': projects})


def custom_logout_view(request):
    logout(request)
    return redirect('jengaHubApp:home')  
    
@login_required
def send_message(request, professional_id):
    # Retrieve the profile of the professional
    profile = get_object_or_404(Professional, id=professional_id)
    
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            subject = form.cleaned_data['subject']
            message_content = form.cleaned_data['message'].strip()
            
            # Check if the message is not empty
            if not message_content:
                messages.error(request, 'Message cannot be empty.')
                return redirect('jengaHubApp:projects')

            # Prepare email content using a template
            email_context = {
                'professional_name': profile.user.get_full_name(),
                'sender_name': request.user.get_full_name(),
                'sender_email': request.user.email,
                'message_content': message_content
            }

            email_body = render_to_string('jengaHubApp/email_template.txt', email_context)

            try:
                # Send the email
                send_mail(
                    subject=subject,
                    message=email_body,
                    from_email=request.user.email,
                    recipient_list=[profile.user.email],
                    fail_silently=False,  # Set to False to raise an error if sending fails
                )
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                # Log the error or handle it as needed
                messages.error(request, f'An error occurred while sending your message: {e}')
            
            return redirect('jengaHubApp:professional_dashboard')
    else:
        form = EmailForm()  # Render an empty form for GET requests
    
    # Render the form with the professional's profile details
    return render(request, 'jengaHubApp/send_email.html', {'form': form, 'profile': profile})


@login_required
def delete_project(request, project_id):
    professional = get_object_or_404(Professional, user=request.user)

    project = get_object_or_404(Project, id=project_id, professional=professional)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project has been deleted successfully.')
        return redirect('jengaHubApp:professional_dashboard')
    return render(request, 'confirm_delete_project.html', {'project': project})

@login_required
def delete_profile(request, professional_id):
    professional = get_object_or_404(Professional, id=professional_id, user=request.user)
    if request.method == 'POST':
        # Delete the user profile and all associated projects
        professional.user.delete()
        messages.success(request, 'Profile and all associated data have been deleted.')
        return redirect('jengaHubApp:home')
    return render(request, 'confirm_delete_profile.html', {'professional': professional})


def advertisement_list(request):
    ads = Advertisement.objects.all()  # Fetch all advertisements
    return render(request, 'jengaHubApp/advertisement_list.html', {'ads': ads})

def rental_list(request):
    rentals = RentalListing.objects.all()  # Fetch all rental listings
    return render(request, 'jengaHubApp/rental_list.html', {'rentals': rentals})
