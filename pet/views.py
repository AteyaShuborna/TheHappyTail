from django.shortcuts import render, redirect
from .models import Adoption
from django.http import HttpResponse

def create_pet_adoption(request):
    if request.method == 'POST':
        pet_type = request.POST['pet_type']
        pet_name = request.POST['pet_name']
        pet_breed = request.POST['pet_breed']
        pet_description = request.POST['pet_description']
        adoption_fee = request.POST['adoption_fee']
        pet_image = request.FILES.get('pet_image')
        
        pet_for_adoption= Adoption(
            pet_type=pet_type,
            pet_name=pet_name,
            pet_breed=pet_breed,
            pet_description=pet_description,
            adoption_fee=adoption_fee,
            pet_image=pet_image,
        )
        pet_for_adoption.save()
        
        return HttpResponse("Successfully posted!")
    else:
        return render(request, 'pet_adoption_create.html')


