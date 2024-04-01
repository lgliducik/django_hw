from django.core.management.base import BaseCommand
from myapp2.models import Order, Product, Client
from datetime import datetime


class Command(BaseCommand):
    help = "Generate fake order and products."

    def handle(self, *args, **kwargs):
        data = datetime.today()
        product1 = Product(name=f'Name', description=f'description ', price=100, date=data)
        product1.save()
        product2 = Product(name=f'Name 2 ', description=f'description 2 ', price=200, date=data)
        product2.save()

        client = Client(name='Lida', email='lida@example.com', tel_number='567123123', address='address 1',
                        date=data)
        client.save()
        order = Order(customer=client, total_price=2, date_ordered=data)
        order.save()
        order.products.add(product1)
        order.products.add(product2)
