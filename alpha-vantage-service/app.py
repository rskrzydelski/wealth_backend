import time
from decimal import Decimal
from av import AvAPI
import mongomarket


class AvMarketCollector:
    def __init__(self):
        self.api = AvAPI()

    def get_market_data_from_api(self):
        self.gold = self.api.get_resource(from_currency='XAU', to_currency='USD')
        self.silver = self.api.get_resource(from_currency='XAG', to_currency='USD')

        self.usdpln = self.api.get_resource(from_currency='USD', to_currency='PLN')
        self.usdeur = self.api.get_resource(from_currency='USD', to_currency='EUR')
        self.usdchf = self.api.get_resource(from_currency='USD', to_currency='CHF')

    def collect_metal_records(self):
        if self.gold:
            self._collect_gold_records(self.gold.price, 'USD', 1.0)
            if self.usdeur:
                self._collect_gold_records(self.gold.price, self.usdeur.ticker_to, self.usdeur.price)
            if self.usdchf:
                self._collect_gold_records(self.gold.price, self.usdchf.ticker_to, self.usdchf.price)
            if self.usdpln:
                self._collect_gold_records(self.gold.price, self.usdpln.ticker_to, self.usdpln.price)

        if self.silver:
            self._collect_silver_records(self.silver.price, 'USD', 1.0)
            if self.usdeur:
                self._collect_silver_records(self.silver.price, self.usdeur.ticker_to, self.usdeur.price)
            if self.usdchf:
                self._collect_silver_records(self.silver.price, self.usdchf.ticker_to, self.usdchf.price)
            if self.usdpln:
                self._collect_silver_records(self.silver.price, self.usdpln.ticker_to, self.usdpln.price)

    def _collect_gold_records(self, api_gold_999_oz_usd_value, currency, exchange_rate):
        """
        collect dict in format {name: val, oz: val, g: val, kg: val}, like e.g:
        {'name': 'gold999', 'oz': '1907.22', 'g': '61.33', 'kg': '61317.28'}
        then assign it to records.
        """
        records = []
        units = ['oz', 'g', 'kg']
        gold_trials = ['999', '585', '333']

        for trial in gold_trials:
            d = {}
            oz_value = Decimal(api_gold_999_oz_usd_value) * Decimal(exchange_rate)
            val = self._convert_price_from_999_to_other(trial, oz_value)
            ls = [self._convert_price_from_oz_to_other_unit(val, u) for u in units]
            z = list(zip(units, ls))
            d["name"] = "gold" + trial
            d["currency"] = currency
            d.update(dict(z))

            for u in units:
                records.append({'name': d.get('name'), 'unit': u, 'currency': d.get('currency'), 'value': d.get(u)})

        # collect market data to mongo database
        for r in records:
            self._set_mongo_metal_data(r)

    def _collect_silver_records(self, api_silver_999_oz_usd_value, currency, exchange_rate):
        records = []
        units = ['oz', 'g', 'kg']
        silver_trials = ['999', '800']

        for trial in silver_trials:
            d = {}
            oz_value = Decimal(api_silver_999_oz_usd_value) * Decimal(exchange_rate)
            val = self._convert_price_from_999_to_other(trial, oz_value)
            ls = [self._convert_price_from_oz_to_other_unit(val, u) for u in units]
            z = list(zip(units, ls))
            d["name"] = "silver" + trial
            d["currency"] = currency
            d.update(dict(z))

            for u in units:
                records.append({'name': d.get('name'), 'unit': u, 'currency': d.get('currency'), 'value': d.get(u)})

        # collect market data to mongo database
        for r in records:
            self._set_mongo_metal_data(r)

    @staticmethod
    def _set_mongo_metal_data(record):
        if not record.get('name') and not record.get('unit') and not record.get('currency') and not record.get('value'):
            return
        mongomarket.set_metal_price(
            name=record.get('name'),
            unit=record.get('unit'),
            currency=record.get('currency'),
            value=record.get('value'))

    @staticmethod
    def _convert_price_from_oz_to_other_unit(oz_price, unit_to):
        value = None
        try:
            if unit_to == 'oz':
                value = Decimal(oz_price).__round__(2)
            if unit_to == 'kg':
                val = Decimal(oz_price) * Decimal(32.15)
                value = val.__round__(2)
            if unit_to == 'g':
                val = Decimal(oz_price) / Decimal(31.1)
                value = val.__round__(2)
        except TypeError:
            return value
        return str(value)

    @staticmethod
    def _convert_price_from_999_to_other(trial: str, price: str) -> str:
        if trial == "999":
            return price
        convert_price = Decimal(price) * (Decimal(trial) / 1000)
        return str(convert_price.__round__(2))


def alpha_vantage_market():
    collector = AvMarketCollector()

    while True:
        collector.get_market_data_from_api()
        collector.collect_metal_records()

        documents = mongomarket.get_content()
        for doc in documents:
            print(doc)
        print(" ")
        print(" ")
        print("go to sleep ")
        time.sleep(120)


if __name__ == '__main__':
    alpha_vantage_market()
