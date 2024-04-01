from django.core.management.base import BaseCommand
from myapp2.models import Order, Product, Client


class Command(BaseCommand):
    help = "Get all order by client id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            orders = Order.objects.filter(customer=client)
            name = f'All order of {client.name}\n'
            text = '\n'.join(str(order.date_ordered) for order in orders)
            self.stdout.write(f'{name}{text}')
