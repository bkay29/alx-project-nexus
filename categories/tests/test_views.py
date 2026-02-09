from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from categories.models import Category


class CategoryAPITest(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name="Books",
            description="All kinds of books"
        )
        self.url = reverse("category-list")

    def test_list_categories(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Books")