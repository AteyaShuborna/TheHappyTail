from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from customuser.models import CustomUser


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
            user = CustomUser(name=name, address=address, email=email)
            user.save()
            user = User.objects.create_user(email, email, password)
            user.save()
        
        return render(request, 'login.html')
    else:
        return render(request,'register.html')
    

def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            messages.info(request, 'invalid email or password')
            return render(request, 'login.html')
        
    else:
        return render(request, 'login.html')
    

def logout_user(request):
    logout(request)
    print('logout success')
    return redirect('index')