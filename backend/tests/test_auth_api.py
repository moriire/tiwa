# Import necessary modules
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework import status
from django.urls import reverse
User = get_user_model()

class AuthenticationAPITestCase(APITestCase):
    def setUp(self):
        self.email = 'testuser@gmail.com'
        self.password = 'testpassword'
        self.user = User.objects.create_user(self.email, password=self.password)
        self.token = Token.objects.get(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_authenticated_user_can_access_protected_endpoint(self):
        url = reverse('your-protected-endpoint')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_access_protected_endpoint(self):
        # Clear authentication headers
        self.client.credentials()

        url = reverse('your-protected-endpoint')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_token_returns_unauthorized(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token InvalidToken')
        url = reverse('your-protected-endpoint')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
