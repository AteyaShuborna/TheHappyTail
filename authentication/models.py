from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(models.Model):
    def __init__(self, name, address):
        self.name = models.CharField(max_length=100)
        self.address = models.CharField(max_length=100)
        self.user = models.OneToOneField(User, on_delete=models.CASCADE)

