from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    fee = models.PositiveIntegerField()
    duration = models.CharField(max_length=200)
    students = models.PositiveIntegerField(default=0)
    entry_requirements = models.CharField(max_length=200)
    exam_body = models.CharField(max_length=200)
    other_requirements = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name


class ImageCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Image(models.Model):
    category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return self.name


class BlogCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Blog(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog/')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title





