# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages
from authentication.forms import UserRegistrationForm


class SignUpView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('homepage')
    
   