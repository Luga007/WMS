from django import forms
from .models import Order, ItemOrders
from product.models import Product


class OrderForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('pending', 'Kutilmoqda'),
        ('processing', 'Qayta ishlanmoqda'),
        ('shipped', 'Yuborilgan'),
        ('delivered', 'Yetkazib berilgan'),
        ('cancelled', 'Bekor qilingan'),
    ]

    status = forms.CharField(widget=forms.Select(choices=STATUS_CHOICES))

    class Meta:
        model = Order
        exclude = ['created_at']


class ItemOrdersForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    order = forms.ModelChoiceField(queryset=Order.objects.all())
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ItemOrders
        fields = '__all__'

