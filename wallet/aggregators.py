from decimal import Decimal

from resources.models import Metal, Cash


# mock values of metals - fetch from web will be implemented
metal_prices = {
    'silver': 110,
    'gold': 6000,
}


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


# aggregation class
class Aggregator(object):
    def __init__(self, owner=None):
        self.owner = owner

    def get_current_metal_value(self, name=None):
        total_cash = 0
        if self._validate_metal_name(name=name):
            if name is None:
                total_cash = 0
                for name in Metal.METAL_CHOICES:
                    total_amount = Metal.objects.get_total_metal_amount(owner=self.owner, name=name[0])
                    try:
                        total_cash += total_amount * metal_prices[name[0]]
                    except:
                        continue
            else:
                total_amount = Metal.objects.get_total_metal_amount(owner=self.owner, name=name)
                try:
                    total_cash = total_amount * metal_prices[name]
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
        total_cash = Cash.objects.get_total_cash(owner=self.owner)
        return Decimal(total_cash).__round__(2) or Decimal(0)

    @staticmethod
    def _validate_metal_name(name=None):
        ok = False
        for item in Metal.METAL_CHOICES:
            if name in item:
                ok = True
        if name is None:
            ok = True
        return ok

