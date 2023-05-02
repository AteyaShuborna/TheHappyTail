from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from post.models import AdoptionRequest,Missinginfo,AdoptionPost
from customuser.models import Notification,CustomUser
from django.utils import timezone

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
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            user_obj=authenticate(username=username,password=password)

            if user_obj and user_obj.is_staff:
                login(request,user_obj)
                return redirect('admin_dashboard')
            else:
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
    adoption_request = AdoptionRequest.objects.get(id=pk)
    adoption_request.approved = True
    adoption_request.save()

    requested_by = CustomUser.objects.get(email= adoption_request.requested_by.email)
    
    posted_by = CustomUser.objects.get(email= adoption_request.posted_by)
   
    pet=AdoptionPost.objects.get(id=adoption_request.pet_id)
    message = f"Your adoption request for {pet.pet_name} has been approved! You can contact the owner now. Mobile: {pet.pet_mobile} Email:{pet.user_id} "
    Notification.objects.create(recipient=requested_by, message=message, timestamp=timezone.now())
    message = f"we have found your pet {pet.pet_name} a new home!You can contact the interested applicant now. Mobile: {adoption_request.mobile} Email:{adoption_request.requested_by.email}"
    Notification.objects.create(recipient=posted_by, message=message, timestamp=timezone.now())

    return redirect('all_adoption_request')



@staff_member_required(login_url = reverse_lazy('admin_login'))
def view_all_users(request):
    all_users=User.objects.filter(is_superuser=False)
    for user in all_users:
        user_name = CustomUser.objects.get(email=user.username).name
        user.name=user_name
        print(user.name)
    context = {'all_users': all_users}
    
    return render(request, 'all_users.html', context)

@staff_member_required(login_url = reverse_lazy('admin_login'))
def admin_view_userprofile(request,pk):
    c_user=User.objects.get(pk=pk)
    customuser=CustomUser.objects.get(email=c_user.username)
    adoptionpost=AdoptionPost.objects.filter(user_id=customuser.email)
    adoptionreq=AdoptionRequest.objects.filter(requested_by_id=customuser.email)
    for req in adoptionreq:
        pet_name = AdoptionPost.objects.get(id=req.pet_id).pet_name
        req.pet_name = pet_name
    context={'c_user':c_user,'customuser':customuser,'adoptionpost':adoptionpost,'adoptionreq':adoptionreq}
    return render(request, 'userprofile.html', context)

@staff_member_required(login_url = reverse_lazy('admin_login'))
def delete_userprofile(request,pk):
    c_user=User.objects.get(pk=pk)
    customuser=CustomUser.objects.get(email=c_user.username)
    customuser.delete()
    c_user.delete()
    
    return redirect("all_users")
 