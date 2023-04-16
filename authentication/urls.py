from django.urls import path
from . import views

urlpatterns = [
    path('',views.register, name = 'register'),
    path('auth',views.register, name = 'auth'),
    path('login/',views.login_user, name= 'login')
]
