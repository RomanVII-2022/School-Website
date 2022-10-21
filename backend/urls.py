"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('admin-home', BackendHomeView.as_view(), name='backendhome'),
    path('admin-courses', AdminCoursesView.as_view(), name='admincourses'),
    path('admin-addcourse', AddCourseView.as_view(), name='addcourse'),
    path('admin-editcourse/<int:pk>', EditCourseView.as_view(), name='editcourse'),
    path('admin-deletecourse/<int:pk>', DeleteCourseView.as_view(), name='deletecourse'),
    path('admin-blogs', AdminBlogsView.as_view(), name='adminblogs'),
    path('admin-addblog', AddBlogView.as_view(), name='addblog'),
    path('admin-editblog/<int:pk>', EditBlogView.as_view(), name='editblog'),
    path('admin-deleteblog/<int:pk>', DeleteBlogView.as_view(), name='deleteblog'),
    path('admin-staff', AdminStaffView.as_view(), name='adminstaff'),
    path('admin-editstaff/<int:pk>', EditStaffView.as_view(), name='editstaff'),
    path('admin-deletestaff/<int:pk>', DeleteStaffView.as_view(), name='deletestaff'),
    path('admin-users', AdminUserView.as_view(), name='adminusers'),
    path('admin-edituser/<int:pk>', EditUserView.as_view(), name='edituser'),
    path('admin-deleteuser/<int:pk>', DeleteUserView.as_view(), name='deleteuser'),
]
