from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import Group

class UserRegistrationTest(APITestCase):
    def setUp(self):
        Group.objects.create(name='Viewer')  # Ensure the group exists

    def test_register_user(self):
        url = reverse('register')
        data = {'username': 'testuser', 'password': 'testpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

