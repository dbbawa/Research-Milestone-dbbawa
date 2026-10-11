from django import forms
from .models import Property, Unit


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'address', 'image', 'bedrooms', 'bathrooms', 'monthly_rent']


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['unit_number']