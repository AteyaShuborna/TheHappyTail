from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from post.models import AdoptionPost,AdoptionRequest
from customuser.models import CustomUser
import os

class PostTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser@test.com',
            email='testuser@test.com',
            password='testpassword'
        )
        self.customuser = CustomUser.objects.create(
            name='testuser', email='testuser@test.com')
        self.client.login(username='testuser@test.com', password='testpassword')
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
        
        
    def test_create_adoption_post(self):
        self.url1 = reverse('create_adoption_post')
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_image.png')
        image_data = open(image_path, 'rb').read()
        self.image = SimpleUploadedFile("test_image.png", image_data, content_type="image/png")

        data = {
    'pet_type': 'cat',
    'pet_name': 'testpet',
    'pet_breed': 'dhakaiya',
    'pet_description': 'test',
    'pet_image': self.image,
    'pet_colour': 'Golden',
    'pet_gender': 'Male',
    'pet_location': 'dhaka',
    'pet_mobile': '1234567890',
    'pet_behaviour': 'Friendly and playful',
    'pet_food': 'fish',
    'pet_physicalcondition': 'Healthy',
    'pet_availability': True,
    'pet_vaccinated': True,
    'pet_age': 2,
    "user": self.customuser,
}

        
        response = self.client.post(self.url1, data)
        self.assertEqual(response.status_code, 302) 
        post = AdoptionPost.objects.all()[1]
        self.assertEqual(post.pet_name, 'testpet') 
        self.assertEqual(post.user_id, self.user.username)
        
    def test_view_all_adoption_post(self):
        self.url2 = reverse('view_all_adoption_post')
        response = self.client.get(self.url2)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_all_adoption_post.html')
        self.assertContains(response, 'Buddy')
        self.assertEqual(len(response.context['pets']), 1)
        self.assertEqual(response.context['pets'][0], self.adoption_post)


    def test_update_pet_details(self):
        self.url3 = reverse('update_adoption_post', args=[self.adoption_post.id])
        self.client.login(username='testuser@test.com', password='testpassword')
        new_pet_name = 'summer'
        new_pet_age = 3
        new_pet_type = 'dog'
        posted_by= AdoptionPost.objects.get(id=self.adoption_post.id)

        self.assertEqual('testuser@test.com', posted_by.user_id) 
        response = self.client.post(self.url3, {'pet_name': new_pet_name, 'pet_age': new_pet_age , 'pet_type':new_pet_type })
        self.assertEqual(response.status_code, 302) 
        updated_post = AdoptionPost.objects.get(id=self.adoption_post.id)
        self.assertEqual(updated_post.pet_name, new_pet_name) 
        self.assertEqual(updated_post.pet_age, new_pet_age) 

    def test_pet_detail_view(self):
        self.url4 = reverse('pet_detail', args=['adoption', self.adoption_post.pk])
        response = self.client.get(self.url4)
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'adoption_pet_detail.html') 
        self.assertContains(response, 'Buddy') 

    def test_pet_detail_view_invalid_post_id(self):
        url5 = reverse('pet_detail', args=['adoption', 999])
        response = self.client.get(url5)
        self.assertEqual(response.status_code, 404)

    def test_valid_request(self):
        self.url6 = reverse('make_adoption_request', args=[self.adoption_post.pk])

        response = self.client.post(self.url6, {'reason': 'Test Reason', 'mobile': '1234567890', 
                                               'requester_email': 'testrequester@example.com', 'had_pet': True, 
                                               'can_pick_up': False})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(AdoptionRequest.objects.count(), 1)

        adoption_request = AdoptionRequest.objects.get(pk=1)
        
        self.assertEqual(adoption_request.requested_by.email, self.user.username)
        self.assertEqual(adoption_request.pet, self.adoption_post)
        self.assertEqual(adoption_request.posted_by, self.adoption_post.user_id)
        self.assertEqual(adoption_request.reason, 'Test Reason')
        self.assertEqual(adoption_request.mobile, '1234567890')
        self.assertEqual(adoption_request.email, 'testrequester@example.com')
        self.assertEqual(adoption_request.had_pet, True)
        self.assertEqual(adoption_request.can_pick_up, False)
        self.assertFalse(adoption_request.approved)