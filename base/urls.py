from django.urls import path
from . import views

urlpatterns = [
    path('',views.WelcomePage.as_view()),
    path('home/',views.Homepage.as_view(), name = 'home'),
]
