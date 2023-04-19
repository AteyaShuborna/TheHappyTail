from django.urls import path
from .views import create_adoption_post,update_adoption_post,view_all_adoption_post,create_missing_post,update_missing_post,view_all_missing_post,delete_post,pet_detail,make_adoption_request

urlpatterns = [
    path('create-adoption-post/', create_adoption_post , name='create_adoption_post'),
    path('view-all-adoption-post/', view_all_adoption_post, name='view_all_adoption_post'),
    path('<int:pk>/update-adoption-post/', update_adoption_post, name='update_adoption_post'),
    path('create-missing-post/', create_missing_post , name='create_missing_post'),
    path('<int:pk>/update-missing-post/', update_missing_post, name='update_missing_post'),
    path('view-all-missing-post/', view_all_missing_post, name='view_all_missing_post'),
    path('<str:type>/<int:pk>/', pet_detail, name='pet_detail'),
    path('<str:type>/<int:pk>/delete-post/', delete_post, name='delete_post'),
    path('<int:pk>/request-pet-adoption/', make_adoption_request, name='make_adoption_request'),
]
