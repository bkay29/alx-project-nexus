from celery import shared_task
from .models import Product

@shared_task
def update_inventory(product_id, quantity):
    product = Product.objects.get(id=product_id)
    product.stock -= quantity
    product.save()