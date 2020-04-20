from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from users.models import InvestorUser


class InvestorRegisterSerializer(ModelSerializer):
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = InvestorUser
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'my_currency',
        ]

    def validate(self, data):
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError('Password must match')
        return data

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', ''),
            'my_currency': self.validated_data.get('my_currency', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)

        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])

        user.my_currency = self.cleaned_data.get('my_currency')
        user.save()
        return user

