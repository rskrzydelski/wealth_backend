from decimal import Decimal


class MarketData(object):
    def __init__(self):
        pass

    __resources = {
        "gold": Decimal(0),
        "silver": Decimal(0),
        "PLN": Decimal(0),
        "USD": Decimal(0),
        "CHF": Decimal(0),
        "EUR": Decimal(0),
    }

    @classmethod
    def set_resource_price(cls, name, value):
        try:
            cls.__resources[name] = value
        except KeyError as e:
            print(e)

    @classmethod
    def get_reource_price(cls, name):
        return cls.__resources.get(name)
