from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import AdoptionPet, MissingPet
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from customuser.models import CustomUser


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
        return redirect('my_adoption_post')

    if request.method == 'POST':
        adoptionpet.pet_name = request.POST['pet_name']
        adoptionpet.pet_age = request.POST['pet_age']
        adoptionpet.save()

        return redirect('my_adoption_post')
    
    creator_name = adoptionpet.user.name

    context = {'pet': adoptionpet, 'creator_name': creator_name}
      
    return render(request, 'update_pet_adoption.html', context)

@login_required
def delete_pet(request, type, pk):

    url_type=type
    pet_type = {'adoption': AdoptionPet, 'missing': MissingPet}.get(type, None)
    if pet_type is None:
        return render(request, '404.html', status=404)
    
    if url_type=='adoption':
        url= reverse('my_adoption_post')
    elif url_type =='missing':
        url= reverse('my_missing_post')

    pet = get_object_or_404(pet_type, pk=pk)

    if pet.user_id != request.user.username:
        return redirect(url)

    if request.method == 'POST':
        pet.delete()
        return redirect(url)
        
    context = {'pet': pet ,'url_go_to':url}
    return render(request, 'delete_pet.html', context)

def pet_detail(request,type,pk):
    pet_type = {'adoption': AdoptionPet, 'missing': MissingPet}.get(type, None)
    if pet_type is None:
        return render(request, '404.html', status=404)
    
    pet = get_object_or_404(pet_type, pk=pk)
    creator_name = pet.user.name

    context = {'pet': pet, 'creator_name': creator_name}
    return render(request, 'pet_detail.html', context)


#===================================== pet missing ===============================================================#
@login_required
def create_pet_missing(request):
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
        pet_accessories = request.POST['pet_accessories']
        pet_datemissing = request.POST['pet_datemissing']
        pet_vaccinated = request.POST['pet_vaccinated']
        pet_age = request.POST['pet_age']
        pet_rewards=request.POST['pet_rewards']
        pet_last_seen_location=request.POST['pet_last_seen_location']
        email = request.user.username
        creator = CustomUser.objects.get(email=email)

        pet_for_adoption= MissingPet(
            pet_type=pet_type,
            pet_name=pet_name,
            pet_breed=pet_breed,
            pet_description=pet_description,
            pet_image=pet_image,
            pet_colour=pet_colour,
            pet_gender= pet_gender,
            pet_location= pet_location,
            pet_mobile =pet_mobile,
            pet_accessories = pet_accessories,
            pet_datemissing = pet_datemissing,
            pet_vaccinated=pet_vaccinated,
            pet_rewards = pet_rewards,
            pet_last_seen_location = pet_last_seen_location,
            pet_age=pet_age,
            pet_still_missing= True,
            user=creator
            )
        
        pet_for_adoption.save()
        
        return HttpResponse("Successfully posted!")
    else:
        return render(request, 'pet_missing_create.html')
    

@login_required
def update_pet_missing(request,pk):
    missingpet = get_object_or_404(MissingPet, pk=pk)
    if missingpet.user_id != request.user.username:
        return redirect('my_missing_post')

    if request.method == 'POST':
        missingpet.pet_name = request.POST['pet_name']
        missingpet.pet_age = request.POST['pet_age']
        missingpet.save()

        return redirect('my_missing_post')
    
    creator_name = missingpet.user.name

    context = {'pet': missingpet, 'creator_name': creator_name}
      
    return render(request, 'update_pet_missing.html', context)

def view_pet_missing(request):
    pets = MissingPet.objects.filter(pet_still_missing= True)
    return render(request, 'pet_missing_view.html', {'pets': pets})



