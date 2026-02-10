from django.test import TestCase
from products.models import Product
from categories.models import Category
from products.tasks import update_inventory


class InventoryTaskTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")

        self.product = Product.objects.create(
            name="Laptop",
            price=1500,
            stock=10,
            category=self.category
        )

    def test_inventory_is_reduced_correctly(self):
        update_inventory(self.product.id, 3)

        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 7)

    def test_inventory_does_not_go_negative(self):
        update_inventory(self.product.id, 20)

        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 0)