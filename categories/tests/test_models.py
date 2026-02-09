from django.test import TestCase
from categories.models import Category


class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(
            name="Electronics",
            description="Electronic devices"
        )

        self.assertEqual(category.name, "Electronics")
        self.assertEqual(str(category), "Electronics")