from django.urls import path
from . import views

urlpatterns = [
    path('',views.WelcomePage.as_view(), name='index'),
    path('home/',views.Homepage.as_view(), name = 'home'),
    path('login/',views.Login.as_view(), name = 'login'),
    path('register/',views.Register.as_view(), name = 'register'),
]
