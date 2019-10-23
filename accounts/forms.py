from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import InvestorUser


class RegisterForm(UserCreationForm):
    email = forms.CharField(max_length=120, required=True, widget=forms.EmailInput())

    class Meta:
        model = InvestorUser
        fields = ('username', 'email', 'password1', 'password2', 'my_currency')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError('Password must match')
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError('Username already exists')
        return username
