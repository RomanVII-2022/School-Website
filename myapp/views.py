from unicodedata import category
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from members.models import Staff

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        courses = Course.objects.all()[:6]
        context["courses"] = courses
        staff = Staff.objects.all()
        context["staff"] = staff
        blogs = Blog.objects.all().order_by('-created_at')[:3]
        context["blogs"] = blogs
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

class CourseCategoryView(TemplateView):
    template_name = 'coursecategory.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = kwargs['pk']
        category = Category.objects.get(id=category_id)
        context["category"] = category
        courses = Course.objects.filter(category=category)
        context["courses"] = courses
        categories = Category.objects.all()
        context["categories"] = categories
        popular = Course.objects.all()[:5]
        context["popular"] = popular
        return context


class ImageView(ListView):
    model = Image
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image_categories = ImageCategory.objects.all()
        context["categories"] = image_categories
        return context


class BlogView(ListView):
    model = Blog
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = BlogCategory.objects.all()
        context["categories"] = categories
        popular = Blog.objects.all().order_by('-created_at')[:4]
        context["popular"] = popular
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogdetail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = BlogCategory.objects.all()
        context["categories"] = categories
        popular = Blog.objects.all().order_by('-created_at')[:4]
        context["popular"] = popular
        return context
    

class BlogCategoryView(TemplateView):
    template_name = 'blogcategory.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = kwargs['pk']
        category = BlogCategory.objects.get(id=category_id)
        context["category"] = category
        blogs = Blog.objects.filter(category=category)
        context["blogs"] = blogs
        categories = BlogCategory.objects.all()
        context["categories"] = categories
        popular = Blog.objects.all().order_by('-created_at')[:4]
        context["popular"] = popular
        return context
    

    
class ContactView(CreateView):
    model = Contact
    fields = '__all__' 
    template_name = 'contact.html'
    success_url = reverse_lazy('contact')


class ErrorView(TemplateView):
    template_name = '404.html'





    
