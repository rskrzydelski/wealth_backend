from decimal import Decimal


class MarketData(object):
    def __init__(self):
        pass

    __resources = {
        "gold": Decimal(0),
        "silver": Decimal(0),
        "CHFPLN": Decimal(0),
        "PLNCHF": Decimal(0),
        "CHFUSD": Decimal(0),
        "USDCHF": Decimal(0),
        'CHFEUR': Decimal(0),
        'EURCHF': Decimal(0),
        'PLNUSD': Decimal(0),
        'USDPLN': Decimal(0),
        'PLNEUR': Decimal(0),
        'EURPLN': Decimal(0),
        'EURUSD': Decimal(0),
        'USDEUR': Decimal(0),
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
