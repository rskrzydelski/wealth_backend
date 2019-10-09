from django.db import models
from django.contrib.auth.models import AbstractUser


class InvestorUser(AbstractUser):
    CURRENCY_CHOICES = [('USD', 'USD $'), ('EUR', 'EUR €'), ('PLN', 'PLN ZŁ'), ('CHF', 'CHF +')]
    my_currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, default='PLN')
