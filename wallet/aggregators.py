from decimal import Decimal

from resources.models import Metal, Cash, Currency
from market.market_data import MarketData


# classes needed for serializing
class MetalWalletData(object):
    def __init__(self, name='silver', currency=None, total_cash=None, total_cash_spend=None, profit=None):
        self.name = name
        self.my_currency = currency
        self.total_cash = total_cash
        self.total_cash_spend = total_cash_spend
        self.profit = profit


class CashWalletData(object):
    def __init__(self, my_currency=None, cash=None):
        self.my_currency = my_currency
        self.cash = cash


class CurrencyWalletData(object):
    def __init__(self, total_value=None, currency_name=None):
        self.total_value = total_value
        self.currency_name = currency_name


class WalletData(object):
    def __init__(self, title=None, my_fortune=None):
        self.title = title
        self.my_fortune=my_fortune


# aggregation class
class Aggregator(object):
    def __init__(self, owner=None):
        self.owner = owner

    def get_current_metal_value(self, name=None):
        """
        Aggregator:
        get_current_metal_value - returns particular metal value or all metals value base on market prices
        :param name:
        :return: (Decimal) silver value, gold value, all metals value
        """
        total_cash = 0
        if self._validate_metal_name(name=name):
            if name is None:
                total_cash = 0
                for name in Metal.METAL_CHOICES:
                    total_amount = Metal.objects.get_total_metal_amount(owner=self.owner, name=name[0])
                    try:
                        total_cash += total_amount * (MarketData.get_reource_price(name[0]) * MarketData.get_reource_price('USDPLN'))
                    except:
                        continue
            else:
                total_amount = Metal.objects.get_total_metal_amount(owner=self.owner, name=name)
                print(total_amount)
                try:
                    total_cash = total_amount * (MarketData.get_reource_price(name) * MarketData.get_reource_price('USDPLN'))
                except:
                    total_cash = 0
        return Decimal(total_cash).__round__(2) or Decimal(0)

    def get_metal_cash_spend(self, name=None):

        spend_cash = 0
        if self._validate_metal_name(name=name):
            if name is None:
                for name in Metal.METAL_CHOICES:
                    try:
                        spend_cash += Metal.objects.get_total_metal_cash_spend(owner=self.owner, name=name[0])
                    except:
                        continue
            else:
                spend_cash = Metal.objects.get_total_metal_cash_spend(owner=self.owner, name=name)
        return Decimal(spend_cash).__round__(2) or Decimal(0)

    def get_my_cash(self):
        """
        Aggregator:
        get_my_cash - returns my total cash
        :return (Decimal) total_cash
        """
        total_cash = Cash.objects.get_total_cash(owner=self.owner)
        return Decimal(total_cash).__round__(2) or Decimal(0)

    def get_currency_value(self, name=None):
        """
        Aggregator:
        get_currency_value - returns currency value of particular currency or aggregate value of all currency
        :param name:
        :return (Decimal) currency value
        """
        total_value = 0
        if self._validate_currency_name(name=name, my_currency=self.owner.my_currency):
            if name is None:
                for name in Currency.CURRENCY_CHOICES:
                    if name[0] == self.owner.my_currency:
                        continue
                    try:
                        total_value += MarketData.get_reource_price(name[0]) * \
                                       Currency.objects.get_total_currency(owner=self.owner, currency=name[0])
                    except:
                        continue
            else:
                total_value = MarketData.get_reource_price(str(name).upper()) * \
                              Currency.objects.get_total_currency(owner=self.owner, currency=name)
        return Decimal(total_value).__round__(2) or Decimal(0)

    @staticmethod
    def _validate_metal_name(name=None):
        ok = False
        for item in Metal.METAL_CHOICES:
            if name in item:
                ok = True
        if name is None:
            ok = True
        return ok

    @staticmethod
    def _validate_currency_name(name=None, my_currency=None):
        ok = False
        for item in Currency.CURRENCY_CHOICES:
            if str(name).upper() in item and str(name).upper() != my_currency:
                ok = True
            if name is None:
                ok = True
        return ok

