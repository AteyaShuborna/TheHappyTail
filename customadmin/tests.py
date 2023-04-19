from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from post.models import AdoptionPost,AdoptionRequest
from customuser.models import CustomUser

class AdminLoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'admin'
        self.password = 'admin'
        self.staff_user = User.objects.create_user(
            username=self.username,
            password=self.password,
            is_staff=True)
        self.staff_user.save()
        self.user = User.objects.create_user(username='testuser@test.com', password='testpassword')
        self.customuser = CustomUser.objects.create(name='testuser', email='testuser@test.com')

        self.user2 = User.objects.create_user(username='testuser2@test.com', password='testpassword2')
        self.customuser2 = CustomUser.objects.create(name='testuser2', email='testuser2@test.com')

        self.adoption_post = AdoptionPost.objects.create(
            pet_type='cat',
            pet_name='Buddy',
            pet_breed='Golden Retriever',
            pet_description='A friendly dog looking for a new home',
            pet_colour='Golden',
            pet_gender='Male',
            pet_location='New York',
            pet_mobile='555-1234',
            pet_behaviour='Friendly and playful',
            pet_food='Dry food',
            pet_physicalcondition='Healthy',
            pet_availability=True,
            pet_vaccinated=True,
            pet_age=2,
            user=self.customuser
        )
        self.adoption_request = AdoptionRequest.objects.create(requested_by=self.customuser2,
                                                                pet=self.adoption_post, 
                                                                posted_by=self.customuser,
                                                                reason='test reason', 
                                                                mobile='1234567890', 
                                                                email='test@test.com', 
                                                                had_pet=True, 
                                                                can_pick_up=True, 
                                                                approved=False)
        
    def test_admin_login_success(self):
        self.url1 = reverse('admin_login')
        response = self.client.get(self.url1)
        self.assertEqual(response.status_code, 200)

        data = {
            'username': self.username,
            'password': self.password,
        }
        response = self.client.post(self.url1, data=data)
        self.assertRedirects(response, reverse('admin_dashboard'))

    def test_admin_login_invalid_password(self):
        self.url1 = reverse('admin_login')
        response = self.client.get(self.url1)
        self.assertEqual(response.status_code, 200)

        data = {
            'username': self.username,
            'password': 'wrong_password',
        }
        response = self.client.post(self.url1, data=data , follow=True)
        self.assertRedirects(response, '/')
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertFalse(response.wsgi_request.user.is_staff)

    def test_view_all_adoption_request_valid(self):
        self.url2 = reverse('all_adoption_request')
        self.client.login(username='admin', password='admin')
        response = self.client.get(self.url2)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_all_adoption_request.html')
        
        adoption_request = AdoptionRequest.objects.get()
        self.assertEqual(adoption_request.reason, 'test reason')
        self.assertEqual(adoption_request.mobile, '1234567890')
        self.assertEqual(adoption_request.email, 'test@test.com')