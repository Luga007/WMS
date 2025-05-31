from django import forms

from inventory.models import Inventory
from .models import Supplier, Product


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'



class ProductForm(forms.ModelForm):
    SIZE_CHOICES = [
        ('K', 'Kichik'),
        ('O', 'O\'rta'),
        ('KA', 'Katta'),
        ('JK', 'Juda Katta'),
    ]

    COLOUR_CHOICES = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Green', 'Green'),
    ]
    size = forms.ChoiceField(choices=SIZE_CHOICES)
    colour = forms.ChoiceField(choices=COLOUR_CHOICES)
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all())



    class Meta:
        model = Product
        fields = '__all__'
