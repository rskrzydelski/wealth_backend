from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import InvestorUser


class RegisterForm(UserCreationForm):
    email = forms.CharField(max_length=120, required=True, widget=forms.EmailInput())

    class Meta:
        model = InvestorUser
        fields = ('username', 'email', 'password1', 'password2', 'my_currency')
