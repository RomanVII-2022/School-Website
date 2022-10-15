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




