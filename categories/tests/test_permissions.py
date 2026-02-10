from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from categories.models import Category

User = get_user_model()


class CategoryPermissionTests(APITestCase):
    def setUp(self):
        self.category_url = reverse("category-list")

        self.category = Category.objects.create(
            name="Electronics",
            description="Electronic items"
        )

        self.admin_user = User.objects.create_superuser(
            email="admin@example.com",
            password="AdminPass123"
        )

        self.normal_user = User.objects.create_user(
            email="user@example.com",
            password="UserPass123"
        )

    def authenticate(self, user):
        self.client.force_authenticate(user=user)

    def test_anyone_can_read_categories(self):
        response = self.client.get(self.category_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_cannot_create_category(self):
        response = self.client.post(
            self.category_url,
            {"name": "Books"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_non_admin_cannot_create_category(self):
        self.authenticate(self.normal_user)

        response = self.client.post(
            self.category_url,
            {"name": "Books"},
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_create_category(self):
        self.authenticate(self.admin_user)

        response = self.client.post(
            self.category_url,
            {"name": "Books"},
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_non_admin_cannot_update_category(self):
        self.authenticate(self.normal_user)

        response = self.client.patch(
            reverse("category-detail", args=[self.category.id]),
            {"name": "Updated"},
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_delete_category(self):
        self.authenticate(self.admin_user)

        response = self.client.delete(
            reverse("category-detail", args=[self.category.id])
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)