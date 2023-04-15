from django.urls import path
from .views import create_pet_adoption

urlpatterns = [
    path('create-pet-adoption/', create_pet_adoption , name='create_pet_adoption'),
    #path('pet-adoptions/', view_pet_adoptions, name='view_pet_adoptions'),
]
