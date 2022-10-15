from unicodedata import category
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        courses = Course.objects.all()[:6]
        context["courses"] = courses
        return context
    


class CourseView(TemplateView):
    template_name = 'courses.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p = Paginator(Course.objects.all(), 6)
        page = self.request.GET.get('page')
        courses = p.get_page(page)
        context["courses"] = courses
        categories = Category.objects.all()
        context["categories"] = categories
        popular = Course.objects.all()[:5]
        context["popular"] = popular
        return context


class CourseDetailView(DetailView):
    model = Course
    template_name = 'coursedetail.html'
    context_object_name = 'course'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context["categories"] = categories
        popular = Course.objects.all()[:5]
        context["popular"] = popular
        return context




    
