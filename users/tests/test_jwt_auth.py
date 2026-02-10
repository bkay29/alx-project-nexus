from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class JWTAuthTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="StrongPass123"
        )

        self.token_url = reverse("token_obtain_pair")
        self.refresh_url = reverse("token_refresh")

    def test_user_can_obtain_jwt_tokens(self):
        response = self.client.post(
            self.token_url,
            {
                "email": "testuser@example.com",
                "password": "StrongPass123",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_invalid_credentials_fail(self):
        response = self.client.post(
            self.token_url,
            {
                "email": "testuser@example.com",
                "password": "WrongPassword",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_token_allows_authenticated_request(self):
        token_response = self.client.post(
            self.token_url,
            {
                "email": "testuser@example.com",
                "password": "StrongPass123",
            },
            format="json",
        )

        access_token = token_response.data["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {access_token}"
        )

        response = self.client.get("/api/categories/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_refresh_token_returns_new_access_token(self):
        token_response = self.client.post(
            self.token_url,
            {
                "email": "testuser@example.com",
                "password": "StrongPass123",
            },
            format="json",
        )

        refresh_token = token_response.data["refresh"]

        response = self.client.post(
            self.refresh_url,
            {"refresh": refresh_token},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)