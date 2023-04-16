from django.urls import path
from .views import create_pet_adoption,view_pet_adoption

urlpatterns = [
    path('create-pet-adoption/', create_pet_adoption , name='create_pet_adoption'),
    path('view-pet-adoption/', view_pet_adoption, name='view_pet_adoption'),
]
