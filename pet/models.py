# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from phonenumbers import PhoneNumber
from authentication.models import CustomUser


class Pet(models.Model):
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
    pet_description = models.TextField(blank=True)
    pet_image = models.ImageField(upload_to='static/img/pet', null=True, blank=True)
    pet_vaccinated = models.BooleanField(null=True, blank=True)
    pet_colour = models.CharField(max_length=20, null=True, blank=True)
    pet_gender = models.CharField(max_length=20)
    pet_location = models.CharField(max_length=255) 
    pet_mobile = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pet_age = models.IntegerField(null=True, blank=True)


    class Meta:
        abstract = True


class AdoptionPet(Pet):
    pet_food = models.CharField(max_length=255, null=True, blank=True)
    pet_behaviour = models.CharField(max_length=255, null=True, blank=True)
    pet_physicalcondition = models.CharField(max_length=255, null=True, blank=True)
    pet_availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pet_name} ({self.pet_type})"


class MissingPet(Pet):
    last_seen_location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.pet_name} ({self.pet_type}) - Last seen at {self.last_seen_location}"

