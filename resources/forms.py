from django import forms

from .models import Metal, Currency
from djmoney import forms as money_forms


class NewMetalForm(forms.ModelForm):
    date_of_bought = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Metal
        fields = ['name',
                  'bought_price',
                  'date_of_bought',
                  'amount',
                  'unit',
                  'description']


class EditMetalForm(NewMetalForm):
    name = forms.ChoiceField(choices=Metal.METAL_CHOICES)


class NewCurrencyForm(forms.ModelForm):
    date_of_bought = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Currency
        fields = ['bought_price',
                  'date_of_bought',
                  'bought_currency',
                  ]

    def __init__(self, *args, **kwargs):
        updated_currency = Currency.CURRENCY_CHOICES[:]
        self.my_currency = kwargs.pop('my_currency', None)
        super(NewCurrencyForm, self).__init__(*args, **kwargs)

        if self.my_currency:
            updated_currency.remove(self.my_currency)
            self.fields['bought_price'] = money_forms.MoneyField(max_digits=10,
                                                                 decimal_places=2,
                                                                 currency_choices=[self.my_currency],
                                                                 default_currency=('PLN', 'PLN ZŁ'))
            self.fields['bought_currency'] = money_forms.MoneyField(max_digits=10,
                                                                    decimal_places=2,
                                                                    currency_choices=updated_currency,
                                                                    default_currency=('CHF', 'CHF +'))


