# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages
from authentication.forms import UserRegistrationForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import CustomUser
from django.shortcuts import render

# class SignUpView(CreateView):
#     form_class = UserRegistrationForm
#     template_name = 'signup.html'
#     success_url = reverse_lazy('homepage')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        user = User.objects.create_user(email, email, password)
        customUser = CustomUser(name, address)
        customUser.user = user
        return render(request, 'index.html')
    else:
        return render(request,'register.html')

    
   