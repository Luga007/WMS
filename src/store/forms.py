from .models import Store, Employees
from product.models import Supplier
from django import forms
from location.models import Location


class StoreForm(forms.ModelForm):
    location = forms.ModelChoiceField(queryset=Location.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Location'}))

    class Meta:
        model = Store
        fields = '__all__'


class EmployeesForm(forms.ModelForm):
    EM_CHOICES = [
        ('Boss', 'Boss'),
        ('Worker', 'Worker'),
        ('Guard', 'Guard'),
    ]

    position = forms.ChoiceField(choices=EM_CHOICES, label='Position')

    class Meta:
        model = Employees
        fields = '__all__'

