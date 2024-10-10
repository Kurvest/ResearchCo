from django import forms
from .models import Professional

# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Professional

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = ['bio', 'profile_image', 'profession', 'contact_info']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell us about yourself'}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'profession': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Profession'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Information'}),
        }
