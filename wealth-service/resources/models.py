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
    owner = models.ForeignKey(InvestorUser, on_delete=models.CASCADE, default=1)
    bought_price = MoneyField(max_digits=10,
                              decimal_places=2,
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

        amount = super(MetalManager, self).filter(owner=owner,
                                                  name=name,
                                                  unit=unit).aggregate(total_amount=Sum('amount'))
        return amount.get('total_amount') or Decimal(0)


# data model common for all metals
class Metal(Resource):
    """
    Metal:
    Precious metals data
    """
    objects = MetalManager()

    METAL_CHOICES = [
        ('silver999', 'Silver999'),
        ('silver800', 'Silver800'),
        ('gold999', 'Gold999'),
        ('gold585', 'Gold585'),
        ('gold333', 'Gold333'),
    ]
    UNIT_CHOICES = [
        ('oz', 'ounce'),
        ('g', 'gram'),
        ('kg', 'kilogram'),
    ]
    name = models.CharField(
        max_length=10,
        choices=METAL_CHOICES,
        default='silver999',
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
        total_currency = super(CurrencyManager, self).filter(owner=owner,
                                                             bought_currency_currency__icontains=currency)\
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

        if total_cash['my_cash'] is None:
            value = Decimal(0)
        else:
            value = Decimal(total_cash['my_cash']).__round__(2)

        return value


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
                         default_currency='PLN')

    def __str__(self):
        return '{} cash {}'.format(self.owner.username, self.my_cash)

