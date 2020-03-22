from django import forms
from .models import ProductGroup, Product


class ProductGroupModelForm(forms.ModelForm):
    class Meta:
        model = ProductGroup
        fields = [
            'group_name',
            'pub_date',
                 ]


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'is_active',
        ]