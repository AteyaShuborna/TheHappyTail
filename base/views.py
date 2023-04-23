from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from post.models import AdoptionPost, MissingPost

# Create your views here.
def welcome(request):
    a_pets = AdoptionPost.objects.filter(pet_availability=True)
    m_pets =  MissingPost.objects.filter(pet_still_missing= True)
    context={'missing_pets':m_pets, 'adoption_pets': a_pets}
    return render(request,'index.html', context)


