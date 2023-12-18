from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(label='Название')
    view = forms.CharField(label='Описание товара')
    price = forms.IntegerField(min_value=0, label='Цена')