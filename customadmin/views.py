from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from post.models import AdoptionRequest,Missinginfo,AdoptionPost


# Create your views here.
def admin_login(request):
    try:
        if request.user.is_authenticated and request.user.is_stuff:
            return redirect('admin_dashboard')
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj= User.objects.filter(username=username)
            if not user_obj.exists():
                messages.info(request,'Account not found')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            user_obj=authenticate(username=username,password=password)

            if user_obj and user_obj.is_staff:
                login(request,user_obj)
                return redirect('admin_dashboard')
            
            messages.info(request,'Invalid Password')
            return redirect('/')
        
        return render(request,'admin_login.html')
    
    except Exception:
        return redirect('index')
    
def logout_admin(request):
    logout(request)
    print('logout success')
    return redirect('admin_login')


@staff_member_required(login_url = reverse_lazy('admin_login'))
def admin_dashboard(request):
    return render(request,'admin_dashboard.html')


@staff_member_required(login_url = reverse_lazy('admin_login'))
def view_all_adoption_request(request):
    all_requests = AdoptionRequest.objects.filter(approved=False)
    
    for req in all_requests:
        pet_name = AdoptionPost.objects.get(id=req.pet_id).pet_name
        req.pet_name = pet_name
    context = {'requests': all_requests}
    return render(request, 'view_all_adoption_request.html', context)

@staff_member_required(login_url = reverse_lazy('admin_login'))
def approve_adoption_request(request,pk):
    user_request=AdoptionRequest.objects.filter(pk=pk)
    user_request.approved=True
    user_request.save()
    return HttpResponse("Approved")