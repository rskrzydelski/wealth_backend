from django import forms
from djmoney import forms as money_forms

from .models import Metal


class NewMetalForm(forms.Form):
    current_price = money_forms.MoneyField(max_digits=10, decimal_places=2, default_currency='PLN')
    bought_price = money_forms.MoneyField(max_digits=10, decimal_places=2, default_currency='PLN')
    date_of_bought = forms.DateTimeField()
    amount = forms.DecimalField(min_value=0, max_digits=10, decimal_places=0)
    # name of metal is assign in view catched from url
    unit = forms.ChoiceField(choices=Metal.UNIT_CHOICES)


class EditMetalForm(NewMetalForm):
    name = forms.ChoiceField(choices=Metal.METAL_CHOICES)



