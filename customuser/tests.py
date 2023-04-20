from django.test import TestCase, Client
from .models import CustomUser
from django.contrib.auth.models import User
from django.urls import reverse
from post.models import AdoptionPost
from django.contrib.auth import get_user_model
# Create your tests here.

class CustomUserTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(name="ateya shuborna", email="shuborna98@gmail.com", address="kadamtala")

    def test_custom_user_str(self):
        shuborna = CustomUser.objects.get(email="shuborna98@gmail.com")
        self.assertEqual(str(shuborna), "ateya shuborna")

class UserAdoptionPostViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test@example.com',
            email='test@example.com',
            password='testpass'
        )
        self.user.save()
        self.customuser = CustomUser(name='test', address='testaddress', email='test@example.com')
        self.customuser.save() 
        self.client.login(username='test@example.com', password='testpass')
        
       
        AdoptionPost.objects.create(
            user=self.customuser,
            pet_name='Fluffy',
            pet_type='cat',
            pet_breed='Persian',
            pet_description='A cute and friendly cat',
            pet_gender='female',
            pet_location='London',
            pet_mobile='1234567890'
        )
        AdoptionPost.objects.create(
            user=self.customuser,
            pet_name='Buddy',
            pet_type='dog',
            pet_breed='Labrador',
            pet_description='A loyal and energetic dog',
            pet_gender='male',
            pet_location='New York',
            pet_mobile='0987654321'
        )

    def test_user_adoption_post_view(self):
        url = reverse('my_adoption_post')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_all_adoption_post.html')
        self.assertContains(response, 'Fluffy')
        self.assertContains(response, 'Buddy')
