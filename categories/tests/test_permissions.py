from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()


class CategoryPermissionTests(APITestCase):

    def test_unauthenticated_user_cannot_create_category(self):
        response = self.client.post(
            "/api/categories/",
            {
                "name": "Electronics",
                "description": "Tech stuff",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_non_admin_user_cannot_create_category(self):
        user = User.objects.create_user(
            email="user@example.com",
            password="StrongPass123",
            is_staff=False,
        )

        self.client.force_authenticate(user=user)

        response = self.client.post(
            "/api/categories/",
            {
                "name": "Fashion",
                "description": "Clothing",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_user_can_create_category(self):
        admin = User.objects.create_user(
            email="admin@example.com",
            password="AdminPass123",
            is_staff=True,
        )

        self.client.force_authenticate(user=admin)

        response = self.client.post(
            "/api/categories/",
            {
                "name": "Books",
                "description": "All books",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_anyone_can_list_categories(self):
        response = self.client.get("/api/categories/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)