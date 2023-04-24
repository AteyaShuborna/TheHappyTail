from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from customuser.models import CustomUser
from django.conf import settings
from django.core.mail import send_mail
import uuid


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']

        if CustomUser.objects.filter(email=email).exists():
            messages.info(request, 'email already exists!')
            return redirect('register')
        if len(password)<6:
            messages.info(request, 'password must be of length 6 at least')
            return redirect('register')
        else:
            user_obj = User.objects.create_user(email, email, password)
            user_obj.save()
            customuser = CustomUser.objects.create(user = user_obj , name=name,address=address,email=email)
            customuser.save()
            return redirect('login')
        
    else:
        return render(request,'register.html')
    

def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('register')
        


        user = authenticate(username = email , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('login')
        
        login(request , user)
        return redirect('/')

    return render(request , 'login.html')
    

def logout_user(request):
    logout(request)
    print('logout success')
    return redirect('index')