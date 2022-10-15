from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import CreateView, FormView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
import re
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
class StaffRegistrationView(CreateView):
    model = Staff
    form_class = StaffRegistrationForm
    template_name = 'staffregister.html'
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        staff = Staff.objects.filter(username=username).exists()
        if staff:
            messages.error(self.request, 'Staff with that user name already exists! Please choose another username.')
            return redirect('staffregister')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        if len(password) < 8:
            messages.error(self.request, 'Password must have atleast 8 characters!')
            return redirect('staffregister')
        digit_error = re.search(r"\d", password) is None
        if digit_error:
            messages.error(self.request, 'Password must contain atleast one digit!')
            return redirect('staffregister')
        uppercase_error = re.search(r"[A-Z]", password) is None
        lowercase_error = re.search(r"[a-z]", password) is None
        if uppercase_error or lowercase_error:
            messages.error(self.request, 'Password must contain uppercase and lowercase characters!')
            return redirect('staffregister')
        symbol_error = re.search(r"\W", password) is None
        if symbol_error:
            messages.error(self.request, 'Password must have atleast one special character. Eg: [@_!$%^&*()<>?/\|}{~:]#')
            return redirect('staffregister')
        password2 = form.cleaned_data.get('password2')
        if password != password2:
            messages.error(self.request, 'The two passwords did not match!')
            return redirect('staffregister')
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        return super().form_valid(form)


class StaffLoginView(FormView):
    form_class = StaffLoginForm
    template_name = 'stafflogin.html'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None and Staff.objects.filter(user=user).exists():
            login(self.request, user)
            staff = Staff.objects.get(user=user)
            pk = staff.id
            return redirect('staffprofile', pk=pk)
        else:
            messages.error(self.request, 'You have entered invalid credentials!')
            return redirect('stafflogin')


class StaffProfileView(DetailView):
    model = Staff
    template_name = 'staffprofile.html'
    context_object_name = 'staff'

    def dispatch(self, request, pk, *args, **kwargs):
        try: 
            if request.user.is_superuser or request.user.staff.id == pk:
                pass
            else:
                return render(request, '404.html')
            return super().dispatch(request, *args, **kwargs)
        except Exception as e:
            return render(request, '404.html')



class StaffEditProfile(UpdateView):
    model = Staff
    form_class = StaffEditProfileForm
    template_name = 'editstaffprofile.html'


    def dispatch(self, request, pk, *args, **kwargs):
        try: 
            if request.user.is_superuser or request.user.staff.id == pk:
                pass
            else:
                return render(request, '404.html')
            return super().dispatch(request, *args, **kwargs)
        except Exception as e:
            return render(request, '404.html')
    

    def form_valid(self, form):
        pk = self.request.user.staff.id
        form.save()
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        user_id = self.request.user.id
        user = User.objects.get(id=user_id)
        user.username = username
        user.email = email
        user.save()
        return redirect('staffprofile', pk=pk)
        
        