# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from customuser.models import CustomUser


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, default=None)
    PET_TYPE_CHOICES = [
        ('cat', 'Cat'),
        ('dog', 'Dog'),
        ('bird', 'Bird'),
        ('other', 'Other'),
    ]

    pet_name = models.CharField(max_length=255)
    pet_type = models.CharField(max_length=10, choices=PET_TYPE_CHOICES)
    pet_breed = models.CharField(max_length=255, null=True, blank=True)
    pet_description = models.TextField(null=True,blank=True)
    pet_image = models.ImageField(upload_to='static/img/pet', null=True, blank=True)
    pet_vaccinated = models.BooleanField(null=True, blank=True)
    pet_colour = models.CharField(max_length=20, null=True, blank=True)
    pet_gender = models.CharField(max_length=20, null=True, blank=True)
    pet_location = models.CharField(max_length=255,null=True, blank=True) 
    pet_mobile = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pet_age = models.IntegerField(null=True, default=0)
    class Meta:
        abstract = True


class AdoptionPost(Post):
    pet_food = models.CharField(max_length=255, null=True, blank=True)
    pet_behaviour = models.CharField(max_length=255, null=True, blank=True)
    pet_physicalcondition = models.CharField(max_length=255, null=True, blank=True)
    pet_availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pet_name} ({self.pet_type})"


class MissingPost(Post):
    pet_last_seen_location = models.CharField(max_length=255)
    pet_datemissing = models.DateField(null=True,blank=True)
    pet_accessories = models.CharField(max_length=255 , null=True , blank= True)
    pet_rewards = models.CharField(max_length=255, null=True , blank=True)
    pet_still_missing = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pet_name} ({self.pet_type}) - Last seen at {self.pet_last_seen_location}"
    

class AdoptionRequest(models.Model):
    posted_by = models.CharField(max_length=20 , default=None)
    requested_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, default=None)
    pet = models.ForeignKey(AdoptionPost, on_delete=models.CASCADE, null=True, default=None)
    reason = models.TextField(blank=True)
    mobile  = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    had_pet = models.BooleanField(default=False, null=True, blank=True)
    can_pick_up = models.BooleanField(null=True, blank=True, default=False)
    approved= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.requested_by} ({self.pet}) - posted by {self.posted_by}"
    
class Missinginfo(models.Model):
    pass

