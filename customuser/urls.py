from django.urls import path
from .views import user_adoption_post

urlpatterns = [
    path('my-adoption-post/', user_adoption_post, name='my_adoption_post'),
    #path('pet/<int:pk>/', pet_detail, name='pet_detail'),
]
