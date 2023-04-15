# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    PET_TYPE_CHOICES = [
        ('cat', 'Cat'),
        ('dog', 'Dog'),
        ('bird', 'Bird'),
        ('other', 'Other'),
    ]

    pet_name = models.CharField(max_length=255)
    pet_type = models.CharField(max_length=10, choices=PET_TYPE_CHOICES)
    pet_breed = models.CharField(max_length=255)
    pet_description = models.TextField(blank=True)
    pet_image = models.ImageField(upload_to='static/img/pet', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Adoption(Pet):
    adoption_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.pet_name} ({self.pet_type})"


class MissingPet(Pet):
    last_seen_location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.pet_name} ({self.pet_type}) - Last seen at {self.last_seen_location}"

