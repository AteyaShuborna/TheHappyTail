from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from post.models import AdoptionPost,MissingPost

@login_required
def user_adoption_post(request):
    user_all_adoption_post = AdoptionPost.objects.filter(user_id=request.user.username)
    return render(request, 'user_all_adoption_post.html', {'user_all_adoption_post': user_all_adoption_post})


@login_required
def user_missing_post(request):
    user_all_missing_post = MissingPost.objects.filter(user_id=request.user.username)
    return render(request, 'user_all_missing_post.html', {'user_all_missing_post': user_all_missing_post})
