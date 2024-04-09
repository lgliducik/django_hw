from random import choice, randint, uniform
from django.core.management.base import BaseCommand
from datetime import datetime
from myapp2.models import Product


class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        products = []
        count = kwargs.get('count')
        for i in range(1, count + 1):

            products.append(Product(
                name=f'продукт номер {i}',
                description='длинное описание продукта, которое и так никто не читает',
                price=uniform(0.01, 999_999.99),
                date=datetime.now(),
                count=uniform(0.01, 9.99),
                ))
        Product.objects.bulk_create(products)
