from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User

from djmoney.models.fields import MoneyField


# [singleton] market prices of resources must be only one
class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class MarketPrices(SingletonModel):
    """
    This class can have only one instance. Market price should be unique and it will be fetch from web server
    """
    gold_price = MoneyField(max_digits=10, decimal_places=2, null=True, default=6300, default_currency='PLN')
    silver_price = MoneyField(max_digits=10, decimal_places=2, null=True, default=88, default_currency='PLN')
    palladium_price = MoneyField(max_digits=10, decimal_places=2, null=True, default=5500, default_currency='PLN')
    platinum_price = MoneyField(max_digits=10, decimal_places=2, null=True, default=4500, default_currency='PLN')

    @property
    def au_sell_rate(self):
        return 0.95 * self.gold_price

    @property
    def ag_sell_rate(self):
        return 0.92 * self.silver_price

    @property
    def gold_silver_ratio(self):
        return self.gold_price / self.silver_price

    def __str__(self):
        return 'MarketPrice singleton'


# data model common for all resources
class Resource(models.Model):
    """
    Common data for resource
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    bought_price = MoneyField(max_digits=10, decimal_places=2, null=True, blank=True, default_currency='PLN')
    date_of_bought = models.DateTimeField(auto_now_add=False)
    amount = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    class Meta:
        abstract = True


# data model common for all metals
class Metal(Resource):
    """
    Precious metals data
    """
    METAL_CHOICES = [
        ('Ag', 'Silver'),
        ('Au', 'Gold'),
    ]
    UNIT_CHOICES = [
        ('oz', 'ounce'),
        ('g', 'gram'),
        ('kg', 'kilogram'),
    ]
    name = models.CharField(
        max_length=10,
        choices=METAL_CHOICES,
        default='Ag',
    )
    unit = models.CharField(max_length=10,
                            choices=UNIT_CHOICES,
                            default='oz')

    description = models.TextField(blank=True, help_text='Type some information about this transaction (optional)')

    @classmethod
    def get_metal_list(cls, owner, name):
        return cls.objects.filter(owner=owner, name=name)

    @classmethod
    def get_total_metal_oz(cls, owner=None, name='Ag'):
        total_oz = cls.objects.filter(owner=owner, name=name, unit='oz').aggregate(amount=Sum('amount'))
        return total_oz['amount']

    def __str__(self):
        return self.get_name_display()


class Cash(Resource):
    CURRENCY_CHOICES = [('USD', 'USD $'), ('EUR', 'EUR €'), ('PLN', 'PLN ZŁ'), ('CHF', 'CHF')]
    currency = models.CharField(
        max_length=10,
        choices=CURRENCY_CHOICES,
        default='CHF',
    )

    @classmethod
    def get_cash_list(cls, owner, currency):
        return cls.objects.filter(owner=owner, currency=currency)

    @classmethod
    def get_total_cash(cls, owner=None, currency='PLN'):
        total_cash = cls.objects.filter(owner=owner, currency=currency).aggregate(amount=Sum('amount'))
        return total_cash['amount']

    def __str__(self):
        return self.currency

# class Land(Resource):
#     LAND_CHOICES = [
#         ('f', 'farmland'),
#         ('b', 'building'),
#     ]
#     AREA_TYPE = [
#         ('h', 'hectare'),
#     ]
#     type = models.CharField(
#         max_length=10,
#         choices=LAND_CHOICES,
#         default='b',
#     )
#     area_unit = models.CharField(max_length=10,
#                                  choices=AREA_TYPE,
#                                  default='h')
