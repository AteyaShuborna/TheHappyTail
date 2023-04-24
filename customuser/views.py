from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from post.models import AdoptionPost,MissingPost
from .models import Notification,CustomUser
from django.contrib.auth.models import User
from django.http import HttpResponse


@login_required
def user_adoption_post(request):
    user_all_adoption_post = AdoptionPost.objects.filter(user_id=request.user.username)
    return render(request, 'user_all_adoption_post.html', {'user_all_adoption_post': user_all_adoption_post})


@login_required
def user_missing_post(request):
    user_all_missing_post = MissingPost.objects.filter(user_id=request.user.username)
    return render(request, 'user_all_missing_post.html', {'user_all_missing_post': user_all_missing_post})


@login_required
def notifications(request):
    user=CustomUser.objects.get(email=request.user.username)
    notifications = Notification.objects.filter(recipient=user).order_by('-timestamp')
    return render(request, 'notification.html', {'notifications': notifications})

@login_required
def userprofile(request,pk):
    if  request.user.id==pk:
        user=User.objects.get(pk=pk)
        customuser=CustomUser.objects.get(email=user.username)
        context={'user':user,'customuser':customuser}
        return render(request, 'userprofile.html', context)
    else:
        return HttpResponse('not authorized')


