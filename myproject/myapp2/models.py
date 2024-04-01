from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    tel_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(max_length=100)

    def __str__(self):
        return f'Client name: {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(max_length=100)

    def __str__(self):
        return f'Product name: {self.name}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order customer: {self.customer.name}'
