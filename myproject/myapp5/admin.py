from django.contrib import admin
from myapp2.models import Product, Order, Client


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'description', 'price']

    ordering = ['price']
    list_filter = ['date', 'price']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Название продукта (name)'

    """Отдельный продукт."""
    fields = ['name', 'description', 'price', 'date', 'count']
    readonly_fields = ['date']


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Client)

