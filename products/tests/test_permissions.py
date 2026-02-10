from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from products.models import Product
from categories.models import Category

User = get_user_model()


class ProductPermissionTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Electronics"
        )

        self.product = Product.objects.create(
            name="Laptop",
            description="Gaming laptop",
            price=1500,
            stock=10,
            category=self.category
        )

        self.product_url = reverse("product-list")
        self.product_detail_url = reverse(
            "product-detail", args=[self.product.id]
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

    def test_anyone_can_view_products(self):
        response = self.client.get(self.product_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_admin_cannot_create_product(self):
        self.authenticate(self.normal_user)

        response = self.client.post(
            self.product_url,
            {
                "name": "Phone",
                "price": 500,
                "stock": 5,
                "category": self.category.id
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_create_product(self):
        self.authenticate(self.admin_user)

        response = self.client.post(
            self.product_url,
            {
                "name": "Phone",
                "price": 500,
                "stock": 5,
                "category": self.category.id
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_non_admin_cannot_update_product(self):
        self.authenticate(self.normal_user)

        response = self.client.patch(
            self.product_detail_url,
            {"price": 1200},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_delete_product(self):
        self.authenticate(self.admin_user)

        response = self.client.delete(self.product_detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)