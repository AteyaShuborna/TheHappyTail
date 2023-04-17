from django.urls import path
from .views import user_adoption_post,user_missing_post

urlpatterns = [
    path('my-adoption-post/', user_adoption_post, name='my_adoption_post'),
    path('my-missing-post/', user_missing_post, name='my_missing_post'),
]
