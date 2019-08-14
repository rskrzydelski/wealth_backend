from django import forms

from .models import Metal, Cash


class NewMetalForm(forms.ModelForm):
    class Meta:
        model = Metal
        fields = ['name', 'bought_price', 'date_of_bought', 'amount', 'unit']


class EditMetalForm(NewMetalForm):
    name = forms.ChoiceField(choices=Metal.METAL_CHOICES)


class NewCashForm(forms.ModelForm):
    class Meta:
        model = Cash
        fields = ['bought_price', 'date_of_bought', 'amount', 'my_currency', 'currency']


