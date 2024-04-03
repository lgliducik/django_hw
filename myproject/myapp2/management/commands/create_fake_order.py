from django.core.management.base import BaseCommand
from myapp2.models import Order, Product, Client
from datetime import datetime, timedelta
from django.utils import timezone



class Command(BaseCommand):
    help = "Generate fake order and products."

    def handle(self, *args, **kwargs):
        data = timezone.now()
        client = Client(name='Lida', email='lida@example.com', tel_number='567123123', address='address 1',
                        date=data)
        client.save()
        order = Order(customer=client, total_price=2, date_ordered=data)
        order.save()

        for i in [1, 10, 100, 300]:
            product1 = Product(name=f'Name {i}', description=f'description {i}', price=i, date=data - timedelta(days=i))
            product1.save()
            order.products.add(product1)

