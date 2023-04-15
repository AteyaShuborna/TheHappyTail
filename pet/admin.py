from django.contrib import admin
from .models import Adoption,MissingPet
# Register your models here.

admin.site.register(Adoption)
class AdoptionAdmin(admin.ModelAdmin):
    list_display = ('pet_name', 'pet_type', 'pet_breed', 'adoption_fee')

admin.site.register(MissingPet)
class MissingPetAdmin(admin.ModelAdmin):
    list_display = ('pet_name', 'pet_type', 'pet_breed', 'last_seen_location')