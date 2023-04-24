from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import AdoptionPost, MissingPost ,AdoptionRequest
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from customuser.models import CustomUser


@login_required
def create_adoption_post(request):
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

        
        pet_for_adoption= AdoptionPost(
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
        return redirect(f"/post/adoption/{pet_for_adoption.id}/")
    else:
        return render(request, 'create_adoption_post.html')
    

def view_all_adoption_post(request):
    pets = AdoptionPost.objects.filter(pet_availability=True)
    context={'pets':pets,'user':request.user}
    return render(request, 'view_all_adoption_post.html', context)

@login_required
def update_adoption_post(request,pk):
    adoptionpet = get_object_or_404(AdoptionPost, pk=pk)
    if adoptionpet.user_id != request.user.username:
        return redirect('my_adoption_post')

    if request.method == 'POST':
        adoptionpet.pet_type = request.POST['pet_type']
        adoptionpet.pet_name = request.POST['pet_name']
        adoptionpet.pet_breed = request.POST['pet_breed']
        adoptionpet.pet_description = request.POST['pet_description']
        adoptionpet.pet_image = request.FILES.get('pet_image')
        adoptionpet.pet_colour = request.POST['pet_colour']
        adoptionpet.pet_gender = request.POST['pet_gender']
        adoptionpet.pet_location = request.POST['pet_location']
        adoptionpet.pet_mobile = request.POST['pet_mobile']
        adoptionpet.pet_behaviour = request.POST['pet_behaviour']
        adoptionpet.pet_food = request.POST['pet_food']
        adoptionpet.pet_physicalcondition = request.POST['pet_physicalcondition']
        adoptionpet.pet_availability = request.POST['pet_availability']
        adoptionpet.pet_vaccinated = request.POST['pet_vaccinated']
        adoptionpet.pet_age = request.POST['pet_age']
        adoptionpet.save()

        return redirect(f"/post/adoption/{adoptionpet.id}/")
    
    creator_name = adoptionpet.user.name

    context = {'pet': adoptionpet, 'creator_name': creator_name}
      
    return render(request, 'create_adoption_post.html', context)

@login_required
def delete_post(request, type, pk):

    url_type=type
    post_type = {'adoption': AdoptionPost, 'missing': MissingPost}.get(type, None)
    if post_type is None:
        return render(request, '404.html', status=404)
    
    if url_type=='adoption':
        url= reverse('my_adoption_post')
    elif url_type =='missing':
        url= reverse('my_missing_post')

    post = get_object_or_404(post_type, pk=pk)

    if post.user_id != request.user.username:
        return redirect(url)

    if request.method == 'POST':
        post.delete()
        return redirect(url)
        
    context = {'pet': post ,'url_go_to':url}
    return render(request, 'delete_post.html', context)

def pet_detail(request,type,pk):
    pet_type = {'adoption': AdoptionPost, 'missing': MissingPost}.get(type, None)
    if pet_type is None:
        return render(request, '404.html', status=404)
    
    pet = get_object_or_404(pet_type, pk=pk)
    creator_name = pet.user.email

    context = {'pet': pet, 'creator_name': creator_name}
    if type=='adoption' :
        return render(request, 'adoption_pet_detail.html', context)
    else:
        return render(request, 'missing_pet_detail.html', context)



#===================================== pet missing ===============================================================#
@login_required
def create_missing_post(request):
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

        pet_missing= MissingPost(
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
        
        pet_missing.save()
        
        return redirect(f"/post/missing/{pet_missing.id}/")
    else:
        return render(request, 'create_missing_post.html')
    

@login_required
def update_missing_post(request,pk):
    missingpet = get_object_or_404(MissingPost, pk=pk)
    if missingpet.user_id != request.user.username:
        return redirect('my_missing_post')

    if request.method == 'POST':
        missingpet.pet_type = request.POST['pet_type']
        missingpet.pet_name = request.POST['pet_name']
        missingpet.pet_breed = request.POST['pet_breed']
        missingpet.pet_description = request.POST['pet_description']
        missingpet.pet_image = request.FILES.get('pet_image')
        missingpet.pet_colour = request.POST['pet_colour']
        missingpet.pet_gender = request.POST['pet_gender']
        missingpet.pet_location = request.POST['pet_location']
        missingpet.pet_mobile = request.POST['pet_mobile']
        missingpet.pet_accessories = request.POST['pet_accessories']
        missingpet.pet_datemissing = request.POST['pet_datemissing']
        missingpet.pet_vaccinated = request.POST['pet_vaccinated']
        missingpet.pet_age = request.POST['pet_age']
        missingpet.pet_rewards=request.POST['pet_rewards']
        missingpet.pet_last_seen_location=request.POST['pet_last_seen_location']
        missingpet.save()

        return redirect('my_missing_post')
    
    creator_name = missingpet.user.name

    context = {'pet': missingpet, 'creator_name': creator_name}
      
    return render(request, 'create_missing_post.html', context)

def view_all_missing_post(request):
    pets = MissingPost.objects.filter(pet_still_missing= True)
    return render(request, 'view_all_missing_post.html', {'pets': pets})


@login_required
def make_adoption_request(request,pk):

    email = request.user.username
    creator = CustomUser.objects.get(email=email)
    pet=AdoptionPost.objects.get(pk=pk)
    posted_by=pet.user_id

    if request.method == 'POST':
        reason = request.POST['reason']
        mobile = request.POST['mobile']
        requester_email = request.POST['requester_email']
        had_pet = request.POST['had_pet']
        can_pick_up = request.POST['can_pick_up']

        
        adoption_request= AdoptionRequest(
            requested_by=creator,
            pet=pet,
            posted_by=posted_by,
            reason=reason,
            mobile=mobile,
            email=requester_email,
            had_pet=had_pet,
            can_pick_up=can_pick_up,
            approved=False)
        print(adoption_request)
        
        adoption_request.save()
            
        return HttpResponse("Successfully requested!")
    
    context={'pet':pet}
    
    return render(request, 'make_adoption_request.html',context)




