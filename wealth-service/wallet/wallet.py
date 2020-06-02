import sys
from decimal import Decimal

from django.db.models import Sum
from resources.models import Metal, Cash, Currency
from market.market_data import MarketData



# classes needed for serializing
class MetalWalletData(object):
    def __init__(self, name='silver', currency=None, metal_value=None, cash_spend=None, profit=None):
        self.name = name
        self.my_currency = currency
        self.metal_value = metal_value
        self.cash_spend = cash_spend
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


class Wallet(object):
    """
    Wallet: class for calc asset value and profit.
    """
    def __init__(self, owner=None):
        self.owner = owner

    def get_metal_value(self, name, resource_id):
        metal = Metal.objects.filter(owner=self.owner, name=name, id=resource_id).first()
        single_unit_value = MarketData.get_metal_market_price(name=name,
                                                              unit=metal.unit,
                                                              currency=self.owner.my_currency,
                                                              service_name='my-service')
        value = single_unit_value * metal.amount
        return value.__round__(2)

    def get_metals_value(self, name):
        value = Decimal(0)
        for unit in Metal.UNIT_CHOICES:
            amount = Metal.objects.get_total_metal_amount(owner=self.owner, name=name, unit=unit[0])
            single_unit_value = MarketData.get_metal_market_price(name=name,
                                                                  unit=unit[0],
                                                                  currency=self.owner.my_currency,
                                                                  service_name='my-service')
            v = single_unit_value * amount
            value += v
        return value.__round__(2)

    def get_all_metals_value(self):
        value = Decimal(0)
        for name in Metal.METAL_CHOICES:
            v = self.get_metals_value(name=name[0])
            value += v
        return value.__round__(2)

    def get_metal_cash_spend(self, name, resource_id):
        metal = Metal.objects.filter(owner=self.owner, name=name, id=resource_id).first()
        return metal.bought_price.amount

    def get_metals_cash_spend(self, name):
        result = Metal.objects.filter(owner=self.owner, name=name).aggregate(value=Sum('bought_price'))
        return result['value'] if result['value'] is not None else Decimal(0)

    def get_all_metals_cash_spend(self):
        result = Metal.objects.filter(owner=self.owner).aggregate(value=Sum('bought_price'))
        return result['value']

    def get_metal_profit(self, name, resource_id):
        return \
            self.get_metal_value(name=name, resource_id=resource_id) - \
            self.get_metal_cash_spend(name=name, resource_id=resource_id)

    def get_metals_profit(self, name):
        return self.get_metals_value(name=name) - self.get_metals_cash_spend(name=name)

    def get_all_metals_profit(self):
        return self.get_all_metals_value() - self.get_all_metals_cash_spend()






    def get_all_my_cash(self):
        return Cash.objects.get_total_cash(owner=self.owner)

#     def view_get_metal_value(self, name=None):
#         if self._validate_metal_name(name=name):
#             if name is not None:
#                 value = self._calc_metal_value(owner=self.owner, name=name)
#             else:
#                 values = [self._calc_metal_value(owner=self.owner, name=name[0]) for name in Metal.METAL_CHOICES]
#                 value = (sum(values) if None not in values else None)
#             return value
#         return None
#
#
# ###
#
#     def get_total_metal_cash_spend(self, owner=None, name=None, unit='oz'):
#         """
#         MetalManager:
#         get_total_metal_cash_spend - returns total cash spend of particular metal or all metals
#         :param name [silver, gold, none]
#         :param owner
#         :param unit [oz]
#         :returns (Decimal) [silver cash spend, gold cash spend, all metals cash spend]
#         """
#         total_spend, total = 0, 0
#
#         if name is None:
#             return Decimal(0)
#         if name:
#             total_spend = super(MetalManager, self)\
#                          .filter(owner=owner, name=name, unit=unit)\
#                          .aggregate(total_cash_spend=Sum('bought_price'))
#             total = total_spend['total_cash_spend']
#         if not total:
#             total = Decimal(0)
#         return total.__round__(2)
# ###
#
#     def view_get_metal_cash_spend(self, name=None):
#         if self._validate_metal_name(name=name):
#             if name is not None:
#                 cash_spend = Metal.objects.get_total_metal_cash_spend(owner=self.owner, name=name)
#             else:
#                 values = [Metal.objects.get_total_metal_cash_spend(owner=self.owner, name=name[0])
#                           for name in Metal.METAL_CHOICES]
#                 cash_spend = (sum(values) if None not in values else None)
#             return cash_spend
#         return None

    # def view_get_my_cash(self):
    #     total_cash = Cash.objects.get_total_cash(owner=self.owner)
    #     return total_cash
    #
    # def view_get_currency_value(self, name=None):
    #     if self._validate_currency_name(name=name, my_currency=self.owner.my_currency):
    #         if name is not None:
    #             value = self._calc_currency_value()
    #         else:
    #             values = [self._calc_currency_value(owner=self.owner, name=name[0])
    #                       for name in Currency.CURRENCY_CHOICES if name[0] != self.owner.my_currency]
    #             value = (sum(values) if None not in values else None)
    #         return value
    #     return None
    #
    # @staticmethod
    # def _calc_metal_value(owner, name):
    #     exchange_rate = 'USD' + owner.my_currency.upper()
    #     oz_amount = Metal.objects.get_total_metal_amount(owner=owner, name=name)
    #     oz_market_value = MarketData.get_reource_price(name)
    #     currency_value = MarketData.get_reource_price(exchange_rate)
    #     try:
    #         value = Decimal(oz_amount * oz_market_value * currency_value).__round__(2)
    #     except TypeError:
    #         value = None
    #     return value
    #
    # @staticmethod
    # def _calc_currency_value(owner, name):
    #     exchange_rate = str(name).upper() + owner.my_currency.upper()
    #     market_value = MarketData.get_reource_price(exchange_rate)
    #     currency_amount = Currency.objects.get_total_currency(owner=owner, currency=name)
    #     try:
    #         value = Decimal(market_value * currency_amount).__round__(2)
    #     except TypeError:
    #         value = None
    #     return value
    #
    # @staticmethod
    # def _validate_metal_name(name=None):
    #     ok = False
    #     for item in Metal.METAL_CHOICES:
    #         if name in item:
    #             ok = True
    #     if name is None:
    #         ok = True
    #     return ok
    #
    # @staticmethod
    # def _validate_currency_name(name=None, my_currency=None):
    #     ok = False
    #     for item in Currency.CURRENCY_CHOICES:
    #         if str(name).upper() in item and str(name).upper() != my_currency:
    #             ok = True
    #         if name is None:
    #             ok = True
    #     return ok

