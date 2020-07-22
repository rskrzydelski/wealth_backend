from decimal import Decimal
import mongomarket


class MarketData(object):
    def __init__(self):
        pass

    @staticmethod
    def get_metal_market_price(name, unit, currency):
        price = mongomarket.get_metal_price(name + unit, currency)
        return Decimal(price[name + unit]) if price is not None else Decimal(0)
