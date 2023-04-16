from django.shortcuts import render, redirect
from .models import AdoptionPet
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from authentication.models import CustomUser


@login_required
def create_pet_adoption(request):
    if request.method == 'POST':
        pet_type = request.POST['pet_type']
        pet_name = request.POST['pet_name']
        pet_breed = request.POST['pet_breed']
        pet_description = request.POST['pet_description']
        pet_image = request.FILES.get('pet_image')
        pet_colour = request.POST['pet_colour']
        pet_gender = request.POST['pet_gender']
        pet_location = request.POST['pet_location']
        pet_mobile = request.POST['pet_mobile']
        pet_behaviour = request.POST['pet_behaviour']
        pet_food = request.POST['pet_food']
        pet_physicalcondition = request.POST['pet_physicalcondition']
        pet_availability = request.POST['pet_availability']
        pet_vaccinated = request.POST['pet_vaccinated']
        email = request.user.username
        creator = CustomUser.objects.get(email=email)

        pet_for_adoption= AdoptionPet(
            pet_type=pet_type,
            pet_name=pet_name,
            pet_breed=pet_breed,
            pet_description=pet_description,
            pet_image=pet_image,
            pet_colour=pet_colour,
            pet_gender= pet_gender,
            pet_location= pet_location,
            pet_mobile =pet_mobile,
            pet_behaviour = pet_behaviour,
            pet_food=pet_food,
            pet_physicalcondition=pet_physicalcondition,
            pet_availability=pet_availability,
            pet_vaccinated=pet_vaccinated,
            user=creator
            )
        
        pet_for_adoption.save()
        
        return HttpResponse("Successfully posted!")
    else:
        return render(request, 'pet_adoption_create.html')
    

def view_pet_adoption(request):
    pets = AdoptionPet.objects.filter(pet_availability=True)
    return render(request, 'pet_adoption_view.html', {'pets': pets})


