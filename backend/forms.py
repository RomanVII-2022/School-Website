from django import forms
from myapp.models import *
from members.models import *
from django.contrib.auth.models import User


class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
            'category':forms.Select(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'fee':forms.TextInput(attrs={'class':'form-control'}),
            'duration':forms.TextInput(attrs={'class':'form-control'}),
            'students':forms.TextInput(attrs={'class':'form-control'}),
            'entry_requirements':forms.TextInput(attrs={'class':'form-control'}),
            'exam_body':forms.TextInput(attrs={'class':'form-control'}),
            'other_requirements':forms.Textarea(attrs={'class':'form-control'}),
        }

class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'first_name', 'last_name', 'image', 'category', 'description')

        widgets = {
            'category':forms.Select(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
        }


class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'first_name', 'last_name', 'image', 'category', 'description')

        widgets = {
            'category':forms.Select(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
        }

class EditStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('username', 'first_name', 'last_name', 'role', 'profile_image', 'email')

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'role':forms.TextInput(attrs={'class':'form-control'}),
            'profile_image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }