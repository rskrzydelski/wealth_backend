from django import forms

from .models import Metal, Cash


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


class NewCashForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewCashForm, self).__init__(*args, **kwargs)
        self.fields['bought_price'].required = False

    date_of_bought = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Cash
        fields = ['bought_price',
                  'date_of_bought',
                  'amount',
                  'currency']

        labels = {
            'bought_price': 'Bought price (not required, fill only if you bought in currency exchange)',
        }

