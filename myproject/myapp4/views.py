import logging
from .forms import ProductForm
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render


logger = logging.getLogger(__name__)


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            date = form.cleaned_data['date']

            photo = form.cleaned_data['photo']
            fs = FileSystemStorage()
            fs.save(photo.name, photo)

            # Делаем что-то с данными
            logger.info(f'Получили {name=}, {description=}, {price=}, {count=}, {date=}.')
            return render(request, 'myapp4/product_form.html', {'form': form, 'message': 'Продукт создан'})
    else:
        form = ProductForm()
        return render(request, 'myapp4/product_form.html', {'form': form})
