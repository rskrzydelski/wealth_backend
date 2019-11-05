from django.db.models import Q

from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import CharField, EmailField
from rest_framework.serializers import ValidationError

from accounts.models import InvestorUser


class UserLoginSerializer(ModelSerializer):
    username = CharField(label='Investor name', required=False, allow_blank=True)
    email = EmailField(label='Email address', required=False, allow_blank=True)

    class Meta:
        model = InvestorUser
        fields = [
            'username',
            'password',
            'email',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        user_obj = None
        username = data.get('username')
        email = data.get('email')
        password = data['password']

        if not email or not username:
            raise ValidationError('Username and emil is required !')

        user = InvestorUser.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()

        if user.exists():
            user_obj = user.first()
        else:
            raise ValidationError('Username/email is not valid !')

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('Incorrect password !')

        return data
