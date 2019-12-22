from decimal import Decimal

from django.db import models
from django.db.models import Sum
from users.models import InvestorUser

from djmoney.models.fields import MoneyField


# data model common for all resources
class Resource(models.Model):
    """
    Resource:
    Common data for metal and currency resource
    """
    CURRENCY_CHOICES = [('USD', 'USD $'), ('EUR', 'EUR €'), ('PLN', 'PLN ZŁ'), ('CHF', 'CHF +')]
    owner = models.ForeignKey(InvestorUser, on_delete=models.CASCADE, default=1)
    bought_price = MoneyField(max_digits=10,
                              decimal_places=2,
                              currency_choices=CURRENCY_CHOICES,
                              default_currency='PLN')
    date_of_bought = models.DateTimeField(auto_now_add=False)

    class Meta:
        abstract = True


class MetalManager(models.Manager):
    def get_metal_list(self, owner=None, name=None):
        """
        MetalManager:
        get_metal_list - returns list of particular metal or all metals
        :param name [silver, gold, none]
        :param owner
        :returns (Queryset) [silver list, gold list, all metals list]
        """
        if name:
            qs = super(MetalManager, self).filter(owner=owner, name=name)
        else:
            qs = super(MetalManager, self).filter(owner=owner)
        return qs

    def get_total_metal_amount(self, owner=None, name=None, unit='oz'):
        """
        MetalManager:
        get_total_metal_amount - returns total amount of particular metal
        :param name [silver, gold, none]
        :param owner
        :param unit [oz]
        :returns (Decimal) [silver amount, gold amount, None]
        """
        if name is None:
            return None
        total_amount = super(MetalManager, self).filter(owner=owner, name=name, unit=unit).aggregate(total_amount=Sum('amount'))
        return total_amount['total_amount'] or 0

    def get_total_metal_cash_spend(self, owner=None, name=None, unit='oz'):
        """
        MetalManager:
        get_total_metal_cash_spend - returns total cash spend of particular metal or all metals
        :param name [silver, gold, none]
        :param owner
        :param unit [oz]
        :returns (Decimal) [silver cash spend, gold cash spend, all metals cash spend]
        """
        total_spend, total = 0, 0

        if name is None:
            return Decimal(0)
        if name:
            total_spend = super(MetalManager, self)\
                         .filter(owner=owner, name=name, unit=unit)\
                         .aggregate(total_cash_spend=Sum('bought_price'))
            total = total_spend['total_cash_spend']
        if not total:
            total = Decimal(0)
        return total


# data model common for all metals
class Metal(Resource):
    """
    Metal:
    Precious metals data
    """
    objects = MetalManager()

    METAL_CHOICES = [
        ('silver', 'Silver'),
        ('gold', 'Gold'),
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

    amount = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    description = models.TextField(blank=True, help_text='Type some information about this transaction (optional)')

    def __str__(self):
        return self.get_name_display()


class CurrencyManager(models.Manager):
    def get_currency_list(self, owner=None, currency=None):
        '''
        CurrencyManager:
        get_currency_list - returns list of particular currency or all currences
        :param currency [USD, EUR, CHF, PLN]
        :param owner
        :returns (Queryset) [usd list, eur list, chf list, pln list, all currency list]
        '''
        if currency:
            qs = super(CurrencyManager, self).filter(owner=owner, bought_currency_currency__icontains=currency)
        else:
            qs = super(CurrencyManager, self).filter(owner=owner)
        return qs

    def get_total_currency(self, owner=None, currency=None):
        '''
        CurrencyManager:
        get_total_currency - returns total amount of particular currency
        :param currency [USD, EUR, CHF, PLN]
        :param owner
        :returns (Decimal) [usd amount, eur amount, chf amount, pln amount, None]
        '''
        if currency is None:
            return None
        total_currency = super(CurrencyManager, self).filter(owner=owner, bought_currency_currency__icontains=currency)\
                                                     .aggregate(bought_currency=Sum('bought_currency'))
        return total_currency['bought_currency'] or Decimal(0)


class Currency(Resource):
    """
    Currency:
    Currency data
    """
    objects = CurrencyManager()

    bought_currency = MoneyField(max_digits=10,
                                 decimal_places=2,
                                 null=True,
                                 blank=True,
                                 currency_choices=Resource.CURRENCY_CHOICES,
                                 default_currency='CHF')

    def __str__(self):
        return 'Currency'


class CashManager(models.Manager):
    def get_cash_list(self, owner=None):
        '''
        CashManager:
        get_cash_list - returns list my cash
        :param owner
        :returns (Queryset) [cash list]
        '''
        return super(CashManager, self).filter(owner=owner)

    def get_total_cash(self, owner=None):
        '''
        CashManager:
        get_total_cash - returns total amount of my cash
        :param owner
        :returns (Decimal) [my cash amount]
        '''
        total_cash = super(CashManager, self).filter(owner=owner).aggregate(my_cash=Sum('my_cash'))
        return total_cash['my_cash'] or Decimal(0)


class Cash(models.Model):
    """
    Cash:
    My cash
    """
    objects = CashManager()

    owner = models.ForeignKey(InvestorUser, on_delete=models.CASCADE, default=1)
    save_date = models.DateTimeField(auto_now_add=False)
    my_cash = MoneyField(max_digits=10,
                         decimal_places=2,
                         null=True, blank=True,
                         currency_choices=Resource.CURRENCY_CHOICES,
                         default_currency='PLN')

    def __str__(self):
        return '{} cash {}'.format(self.owner.username, self.my_cash)

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
