from django.urls import path
from .views import create_pet_adoption,view_pet_adoption,update_pet_adoption, pet_detail ,delete_pet,create_pet_missing,update_pet_missing,view_pet_missing

urlpatterns = [
    path('create-pet-adoption/', create_pet_adoption , name='create_pet_adoption'),
    path('view-pet-adoption/', view_pet_adoption, name='view_pet_adoption'),
    path('<int:pk>/update-pet-adoption/', update_pet_adoption, name='update_pet_adoption'),
    path('create-pet-missing/', create_pet_missing , name='create_pet_missing'),
    path('<int:pk>/update-pet-missing/', update_pet_missing, name='update_pet_missing'),
    path('view-pet-missing/', view_pet_missing, name='view_pet_missing'),
    path('<str:type>/<int:pk>/', pet_detail, name='pet_detail'),
    path('<str:type>/<int:pk>/delete/', delete_pet, name='delete_pet'),
]
