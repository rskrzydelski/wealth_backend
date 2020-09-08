from decimal import Decimal
import mongomarket


class MarketData(object):
    def __init__(self):
        pass

    @staticmethod
    def get_metal_market_price(name, unit, currency):
        doc = mongomarket.get_metal_price(name, unit, currency)
        if not doc:
            return Decimal(0)
        return Decimal(doc.get('value')) if doc.get('value') is not None else Decimal(0)
