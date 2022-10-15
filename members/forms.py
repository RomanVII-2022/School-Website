from django import forms
from .models import *


class StaffRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your username'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your last name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your email'}))
    role = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Role'}))
    password1 = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your password'}), label='Password')
    password2 = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm your password'}), label='Confirm Password')
    class Meta:
        model = Staff
        fields = ('username', 'first_name', 'last_name', 'email', 'role', 'password1', 'password2')


class StaffLoginForm(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your username'}))
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your password'}), label='Password')


class StaffEditProfileForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('profile_image', 'username', 'first_name', 'last_name', 'email', 'role')

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your username'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your last name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email'}),
            'role': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your role'}),
        }
        
    
        
    