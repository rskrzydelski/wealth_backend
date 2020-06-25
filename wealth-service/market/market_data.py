from decimal import Decimal


class MarketData(object):
    def __init__(self):
        pass

    @staticmethod
    def get_metal_market_price(name, unit, currency):
        if name == 'gold999':
            if unit == 'oz':
                return Decimal(7300)
            if unit == 'g':
                return Decimal(204.5)
            if unit == 'kg':
                return Decimal(234726)
        if name == 'gold585':
            if unit == 'oz':
                return Decimal(3732)
            if unit == 'g':
                return Decimal(120)
            if unit == 'kg':
                return Decimal(120000)
        if name == 'gold333':
            if unit == 'oz':
                return Decimal(2145.9)
            if unit == 'g':
                return Decimal(69)
            if unit == 'kg':
                return Decimal(69000)
        if name == 'silver999':
            if unit == 'oz':
                return Decimal(100)
            if unit == 'g':
                return Decimal(3.2)
            if unit == 'kg':
                return Decimal(3200)
        if name == 'silver800':
            if unit == 'oz':
                return Decimal(43.54)
            if unit == 'g':
                return Decimal(1.4)
            if unit == 'kg':
                return Decimal(1400)

        return Decimal(0)
