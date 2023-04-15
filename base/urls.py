from django.urls import path
from . import views

urlpatterns = [
    path('',views.WelcomePage.as_view(), name='index'),
    path('home/',views.Homepage.as_view(), name = 'home'),
]
