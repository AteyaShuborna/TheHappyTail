from django.urls import path
from .views import create_pet_adoption,view_pet_adoption,update_pet_adoption, pet_detail ,delete_pet

urlpatterns = [
    path('create-pet-adoption/', create_pet_adoption , name='create_pet_adoption'),
    path('view-pet-adoption/', view_pet_adoption, name='view_pet_adoption'),
    path('<int:pk>/update-pet-adoption/', update_pet_adoption, name='update_pet-adoption'),
    path('<str:type>/<int:pk>/', pet_detail, name='pet_detail'),
    path('<str:type>/<int:pk>/delete/', delete_pet, name='delete_pet'),
]
