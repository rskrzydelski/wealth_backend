import time
from decimal import Decimal
from av import AvAPI
import mongomarket


class AvMarketCollector:
    gold_trials = ['999', '585', '333']
    silver_trials = ['999', '800']
    units = ['oz', 'g', 'kg']

    def __init__(self):
        self.api = AvAPI()
        self.gold = None
        self.silver = None
        self.usdpln = None
        self.usdeur = None
        self.usdchf = None
        self.currences_price = {
            'PLN': '',
            'CHF': '',
            'EUR': '',
        }

        # collect USD gold prices as starting point
        self.gold999oz = 0
        self.gold999g = 0
        self.gold999kg = 0
        self.gold585oz = 0
        self.gold585g = 0
        self.gold585kg = 0
        self.gold333oz = 0
        self.gold333g = 0
        self.gold333kg = 0

        self.silver999oz = 0
        self.silver999g = 0
        self.silver999kg = 0
        self.silver800oz = 0
        self.silver800g = 0
        self.silver800kg = 0

        self.gold_usd_values_as_dict = {
            "gold999oz": '',
            "gold999g": '',
            "gold999kg": '',
            "gold585oz": '',
            "gold585g": '',
            "gold585kg": '',
            "gold333oz": '',
            "gold333g": '',
            "gold333kg": '',
        }

        self.silver_usd_values_as_dict = {
            "silver999oz": '',
            "silver999g": '',
            "silver999kg": '',
            "silver800oz": '',
            "silver800g": '',
            "silver800kg": '',
        }

    def start_collect_metal_data(self):
        # call to api for needed data
        self.gold = self.api.get_gold()
        self.silver = self.api.get_silver()
        self.usdpln = self.api.get_usdpln()
        self.usdeur = self.api.get_usdeur()
        self.usdchf = self.api.get_usdchf()

        if not self.gold and not self.silver and not self.usdpln and not self.usdchf and not self.usdeur:
            print("Api not ready")
            return

        self._collect_gold_prices_usd()
        self._collect_silver_prices_usd()

        # collect data into dicts
        self.currences_price['PLN'] = self.usdpln
        self.currences_price['CHF'] = self.usdchf
        self.currences_price['EUR'] = self.usdeur

        self.gold_usd_values_as_dict["gold999oz"] = self.gold999oz
        self.gold_usd_values_as_dict["gold999g"] = self.gold999g
        self.gold_usd_values_as_dict["gold999kg"] = self.gold999kg
        self.gold_usd_values_as_dict["gold585oz"] = self.gold585oz
        self.gold_usd_values_as_dict["gold585g"] = self.gold585g
        self.gold_usd_values_as_dict["gold585kg"] = self.gold585kg
        self.gold_usd_values_as_dict["gold333oz"] = self.gold333oz
        self.gold_usd_values_as_dict["gold333g"] = self.gold333g
        self.gold_usd_values_as_dict["gold333kg"] = self.gold333kg

        self.silver_usd_values_as_dict["silver999oz"] = self.silver999oz
        self.silver_usd_values_as_dict["silver999g"] = self.silver999g
        self.silver_usd_values_as_dict["silver999kg"] = self.silver999kg
        self.silver_usd_values_as_dict["silver800oz"] = self.silver800oz
        self.silver_usd_values_as_dict["silver800g"] = self.silver800g
        self.silver_usd_values_as_dict["silver800kg"] = self.silver800kg

        self._collect_gold_prices_except_usd('PLN')
        self._collect_gold_prices_except_usd('EUR')
        self._collect_gold_prices_except_usd('CHF')

        self._collect_silver_prices_except_usd('PLN')
        self._collect_silver_prices_except_usd('EUR')
        self._collect_silver_prices_except_usd('CHF')

    def _collect_gold_prices_usd(self):
        self.gold999oz = Decimal(self.gold.price)
        self.gold999g = (Decimal(self.gold999oz) / Decimal(31.1))
        self.gold999kg = (Decimal(self.gold999oz) / Decimal(31.1)) * 1000
        self.gold585oz = (Decimal(self.gold999oz) * Decimal(0.585))
        self.gold585g = (Decimal(self.gold999g) * Decimal(0.585))
        self.gold585kg = (Decimal(self.gold585oz) / Decimal(31.1)) * 1000
        self.gold333oz = (Decimal(self.gold999oz) * Decimal(0.333))
        self.gold333g = (Decimal(self.gold999g) * Decimal(0.333))
        self.gold333kg = (Decimal(self.gold333oz) / Decimal(31.1)) * 1000

        mongomarket.set_metal_price('gold999oz', str(self.gold999oz.__round__(2)), 'USD', 'oz')
        mongomarket.set_metal_price('gold999g', str(self.gold999g.__round__(2)), 'USD', 'g')
        mongomarket.set_metal_price('gold999kg', str(self.gold999kg.__round__(2)), 'USD', 'kg')
        mongomarket.set_metal_price('gold585oz', str(self.gold585oz.__round__(2)), 'USD', 'oz')
        mongomarket.set_metal_price('gold585g', str(self.gold585g.__round__(2)), 'USD', 'g')
        mongomarket.set_metal_price('gold585kg', str(self.gold585kg.__round__(2)), 'USD', 'kg')
        mongomarket.set_metal_price('gold333oz', str(self.gold333oz.__round__(2)), 'USD', 'oz')
        mongomarket.set_metal_price('gold333g', str(self.gold333g.__round__(2)), 'USD', 'g')
        mongomarket.set_metal_price('gold333kg', str(self.gold333kg.__round__(2)), 'USD', 'kg')

    def _collect_silver_prices_usd(self):
        self.silver999oz = Decimal(self.silver.price)
        self.silver999g = (Decimal(self.silver999oz) / Decimal(31.1))
        self.silver999kg = (Decimal(self.silver999oz) / Decimal(31.1)) * 1000
        self.silver800oz = (Decimal(self.silver999oz) * Decimal(0.800))
        self.silver800g = (self.silver999g * Decimal(0.800))
        self.silver800kg = (Decimal(self.silver800oz) / Decimal(31.1)) * 1000

        mongomarket.set_metal_price('silver999oz', str(self.silver999oz.__round__(2)), 'USD', 'oz')
        mongomarket.set_metal_price('silver999g', str(self.silver999g.__round__(2)), 'USD', 'g')
        mongomarket.set_metal_price('silver999kg', str(self.silver999kg.__round__(2)), 'USD', 'kg')
        mongomarket.set_metal_price('silver800oz', str(self.silver800oz.__round__(2)), 'USD', 'oz')
        mongomarket.set_metal_price('silver800g', str(self.silver800g.__round__(2)), 'USD', 'g')
        mongomarket.set_metal_price('silver800kg', str(self.silver800kg.__round__(2)), 'USD', 'kg')

    def _collect_gold_prices_except_usd(self, currency):
        for trial in self.gold_trials:
            if trial == '585' or trial == '333':
                spread = Decimal(0.94)
            else:
                spread = 1
            for unit in self.units:
                gold_price = (Decimal(self.gold_usd_values_as_dict['gold' + trial + unit]) * \
                             Decimal(self.currences_price[currency].price)) * spread
                mongomarket.set_metal_price(f'gold{trial}{unit}', str(gold_price.__round__(2)), currency, unit)

    def _collect_silver_prices_except_usd(self, currency):
        for trial in self.silver_trials:
            if trial == '800':
                spread = Decimal(0.85)
            else:
                spread = 1
            for unit in self.units:
                silver_price = (Decimal(self.silver_usd_values_as_dict['silver' + trial + unit]) * \
                             Decimal(self.currences_price[currency].price)) * spread
                mongomarket.set_metal_price(f'silver{trial}{unit}', str(silver_price.__round__(2)), currency, unit)


def alpha_vantage_market():
    collector = AvMarketCollector()

    while True:
        collector.start_collect_metal_data()

        documents = mongomarket.get_content()
        for doc in documents:
            print(doc)
        print(" ")
        print(" ")
        print("go to sleep ")
        time.sleep(120)


if __name__ == '__main__':
    alpha_vantage_market()
