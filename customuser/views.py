from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pet.models import AdoptionPet

@login_required
def user_adoption_post(request):
    user_all_adoption_post = AdoptionPet.objects.filter(user_id=request.user.username)
    return render(request, 'user_all_adoption_post.html', {'user_all_adoption_post': user_all_adoption_post})
