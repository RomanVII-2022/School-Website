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
    path('', HomeView.as_view(), name='home'),
    path('our-courses', CourseView.as_view(), name='courses'),
    path('course-detail/<int:pk>', CourseDetailView.as_view(), name='coursedetail'),
    path('gallery', ImageView.as_view(), name='gallery'),
    path('contact', ContactView.as_view(), name='contact'),
    path('blog', BlogView.as_view(), name='blog'),
    path('blogdetail/<int:pk>', BlogDetailView.as_view(), name='blogdetail'),
    path('blog-category/<int:pk>', BlogCategoryView.as_view(), name='blogcategory'),
    path('course-category/<int:pk>', CourseCategoryView.as_view(), name="coursecategory"),
    path('404', ErrorView.as_view(), name='404'),
]
