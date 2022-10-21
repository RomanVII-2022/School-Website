from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from myapp.models import *
from members.models import *
from .forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User

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
    

class AdminCoursesView(ListView):
    model = Course
    template_name = 'admincourses.html'


class AddCourseView(SuccessMessageMixin, CreateView):
    model = Course
    form_class = EditCourseForm
    template_name = 'addcourse.html'
    success_message = 'Course has been created successfully'
    success_url = reverse_lazy('admincourses')

class EditCourseView(SuccessMessageMixin, UpdateView):
    model = Course
    form_class = EditCourseForm
    template_name = 'editcourses.html'
    success_message = 'Course has been updated successfully'
    success_url = reverse_lazy('admincourses')

class DeleteCourseView(SuccessMessageMixin, DeleteView):
    model = Course
    template_name = 'deletecourse.html'
    success_message = 'Course has been deleted successfully'
    success_url = reverse_lazy('admincourses')


class AdminBlogsView(ListView):
    model = Blog
    template_name = 'adminblogs.html'


class AddBlogView(SuccessMessageMixin, CreateView):
    model = Blog
    form_class = AddBlogForm
    template_name = 'addblog.html'
    success_message = 'Blog has been created successfully'
    success_url = reverse_lazy('adminblogs')


class EditBlogView(SuccessMessageMixin, UpdateView):
    model = Blog
    form_class = EditBlogForm
    template_name = 'editblogs.html'
    success_message = 'Blog has been updated successfully'
    success_url = reverse_lazy('adminblogs')

class DeleteBlogView(SuccessMessageMixin, DeleteView):
    model = Blog
    template_name = 'deleteblog.html'
    success_message = 'Blog has been deleted successfully'
    success_url = reverse_lazy('adminblogs')

class AdminStaffView(ListView):
    model = Staff
    template_name = 'adminstaff.html'

class EditStaffView(SuccessMessageMixin, UpdateView):
    model = Staff
    form_class = EditStaffForm
    template_name = 'editstaff.html'
    success_message = 'Staff has been updated successfully'
    success_url = reverse_lazy('adminstaff')

class DeleteStaffView(SuccessMessageMixin, DeleteView):
    model = Staff
    template_name = 'deletestaff.html'
    success_message = 'Staff has been deleted successfully'
    success_url = reverse_lazy('adminstaff')


class AdminUserView(ListView):
    model = User
    template_name = 'adminusers.html'


class EditUserView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = EditUserForm
    template_name = 'edituser.html'
    success_message = 'User has been updated successfully'
    success_url = reverse_lazy('adminusers')


class DeleteUserView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'deleteuser.html'
    success_message = 'User has been deleted successfully'
    success_url = reverse_lazy('adminusers')


