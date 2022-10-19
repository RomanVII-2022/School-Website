from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from myapp.models import *
from members.models import *

# Create your views here.
class BackendHomeView(TemplateView):
    template_name = 'backendhome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.all().count()
        context["users"] = users
        courses = Course.objects.all().count()
        context["courses"] = courses
        staff = Staff.objects.all().count()
        context["staff"] = staff
        blogs = Blog.objects.all().count()
        context["blogs"] = blogs
        return context
    
