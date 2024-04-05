from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    count = forms.IntegerField()
    date = forms.DateField()
    photo = forms.ImageField()
