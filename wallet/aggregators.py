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
        self.my_fortune = my_fortune


# aggregation class
class Aggregator(object):
    """
    Aggregator: methods for calc asset value by name or if None give all particular asset value.
    """
    def __init__(self, owner=None):
        self.owner = owner

    def view_get_metal_value(self, name=None):
        if self._validate_metal_name(name=name):
            if name is not None:
                value = self._calc_metal_value(owner=self.owner, name=name)
            else:
                values = [self._calc_metal_value(owner=self.owner, name=name[0]) for name in Metal.METAL_CHOICES]
                value = (sum(values) if None not in values else None)
            return value
        return None

    def view_get_metal_cash_spend(self, name=None):
        if self._validate_metal_name(name=name):
            if name is not None:
                cash_spend = Metal.objects.get_total_metal_cash_spend(owner=self.owner, name=name)
            else:
                values = [Metal.objects.get_total_metal_cash_spend(owner=self.owner, name=name[0])
                          for name in Metal.METAL_CHOICES]
                cash_spend = (sum(values) if None not in values else None)
            return cash_spend
        return None

    def view_get_my_cash(self):
        total_cash = Cash.objects.get_total_cash(owner=self.owner)
        return total_cash

    def view_get_currency_value(self, name=None):
        if self._validate_currency_name(name=name, my_currency=self.owner.my_currency):
            if name is not None:
                value = self._calc_currency_value()
            else:
                values = [self._calc_currency_value(owner=self.owner, name=name[0])
                          for name in Currency.CURRENCY_CHOICES if name[0] != self.owner.my_currency]
                value = (sum(values) if None not in values else None)
            return value
        return None

    @staticmethod
    def _calc_metal_value(owner, name):
        exchange_rate = 'USD' + owner.my_currency.upper()
        oz_amount = Metal.objects.get_total_metal_amount(owner=owner, name=name)
        oz_market_value = MarketData.get_reource_price(name)
        currency_value = MarketData.get_reource_price(exchange_rate)
        try:
            value = Decimal(oz_amount * oz_market_value * currency_value).__round__(2)
        except TypeError:
            value = None
        return value

    @staticmethod
    def _calc_currency_value(owner, name):
        exchange_rate = str(name).upper() + owner.my_currency.upper()
        market_value = MarketData.get_reource_price(exchange_rate)
        currency_amount = Currency.objects.get_total_currency(owner=owner, currency=name)
        try:
            value = Decimal(market_value * currency_amount).__round__(2)
        except TypeError:
            value = None
        return value

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

