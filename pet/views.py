from django.shortcuts import render, redirect, get_object_or_404
from .models import AdoptionPet, MissingPet
from django.http import HttpResponse
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
        pet_age = request.POST['pet_age']
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
            pet_age=pet_age,
            user=creator
            )
        
        pet_for_adoption.save()
        
        return HttpResponse("Successfully posted!")
    else:
        return render(request, 'pet_adoption_create.html')
    

def view_pet_adoption(request):
    pets = AdoptionPet.objects.filter(pet_availability=True)
    return render(request, 'pet_adoption_view.html', {'pets': pets})

@login_required
def update_pet_adoption(request,pk):
    adoptionpet = get_object_or_404(AdoptionPet, pk=pk)
    if adoptionpet.user_id != request.user.username:
        return redirect('pet_adoption_view.html')

    if request.method == 'POST':
        adoptionpet.pet_name = request.POST['pet_name']
        adoptionpet.pet_age = request.POST['pet_age']
        adoptionpet.save()

        return render('adoption_pet_detail.html')
    
    creator_name = adoptionpet.user.name

    context = {'pet': adoptionpet, 'creator_name': creator_name}
    
    
    return render(request, 'update_pet_adoption.html', context)

def pet_detail(request,type,pk):
    pet_type = {'adoption': AdoptionPet, 'missing': MissingPet}.get(type, None)
    if pet_type is None:
        return render(request, '404.html', status=404)
    
    pet = get_object_or_404(pet_type, pk=pk)
    creator_name = pet.user.name

    context = {'pet': pet, 'creator_name': creator_name}
    return render(request, 'pet_detail.html', context)




