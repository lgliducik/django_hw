from django.shortcuts import render
from myapp2.models import Client, Order
from datetime import timedelta
from django.utils import timezone


def view_show_products(request, client_name):
    products_365 = []

    client = Client.objects.filter(name=client_name).first()
    if client is not None:
        orders = Order.objects.filter(customer=client)

        for order in orders:
            products_365.extend(order.products.filter(date__gte=timezone.now() - timedelta(days=365)))

    date_30 = timezone.now() - timedelta(days=30)
    products_30 = [i for i in products_365 if i.date > date_30]

    date_7 = timezone.now() - timedelta(days=7)
    products_7 = [i for i in products_30 if i.date > date_7]

    context = {'client': client, 'products_7': products_7, 'products_30': products_30, 'products_365': products_365}
    return render(request, 'myapp3/view_show_products.html', context)
