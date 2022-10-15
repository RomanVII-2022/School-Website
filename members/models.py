from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    profile_image = models.ImageField(null=True, blank=True, upload_to='staffprofile/')
    email = models.EmailField(max_length=200)
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)
    active = models.BooleanField(default=False, help_text="0=default, 1=Active")
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name



