from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User, Group

# Create your tests here.

class ArticleListTest(APITestCase):
    def setUp(self):
        Group.objects.create(name='Viewer')
        Group.objects.create(name='Poster')
        # Register a user
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        poster_group = Group.objects.get(name='Poster')
        self.user.groups.add(poster_group)

    def test_article_list_authenticated(self):
        # Log in the user (for SessionAuthentication)
        self.client.login(username='testuser', password='testpass123')
        url = reverse('articles-list')  # Use the correct route name for your articles list
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

