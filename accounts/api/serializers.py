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


class UserCreateSerializer(ModelSerializer):
    email2 = EmailField(label='Confirm email')
    email = EmailField(label='Email address')

    class Meta:
        model = InvestorUser
        fields = [
            'username',
            'password',
            'email',
            'email2',
            'my_currency',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        email = data.get('email')
        user_qs = InvestorUser.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError('This user has already registered.')
        return data

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get('email')
        email2 = value

        if email1 != email2:
            raise ValidationError('Emails must much !')
        return value

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        my_currency = validated_data.get('my_currency')
        password = validated_data.get('password')
        user_obj = InvestorUser(username=username, email=email, my_currency=my_currency)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = InvestorUser
        fields = [
            'username',
            'email',
            'my_currency',
        ]
