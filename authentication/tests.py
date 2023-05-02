from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from customuser.models import CustomUser

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user_data = {
            'name': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'address': 'test address'
        }
        self.login_data = {
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
        
    def test_register_view(self):
        response = self.client.post('/register/', self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(CustomUser.objects.filter(email='testuser@example.com').exists())
        self.assertTrue(User.objects.filter(username='testuser@example.com').exists())

    def test_register_existing_email(self):
        CustomUser.objects.create(name='testuser2', email='testuser@example.com')
        response = self.client.post(self.register_url , self.user_data)
        self.assertEqual(response.status_code, 302)
        
        
    def test_login_view(self):
        CustomUser.objects.create(name='testuser', email='testuser@example.com')
        User.objects.create_user('testuser@example.com', 'testuser@example.com', 'testpassword')
        response = self.client.post(self.login_url, self.login_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        
    def test_login_invalid_credentials(self):
        CustomUser.objects.create(name='testuser', email='testuser@example.com')
        User.objects.create_user('testuser@example.com', 'testuser@example.com', 'testpassword')
        self.login_data['password'] = 'wrongpassword'
        response = self.client.post(self.login_url, self.login_data)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

        
