from django.core.management.base import BaseCommand
from myapp2.models import Client
from datetime import datetime


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        date = datetime.today()
        client = Client(name='John', email='john@example.com', tel_number='123123123', address='address 1', date=date)
        client.save()
        self.stdout.write(f'{client}')
