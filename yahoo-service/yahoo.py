import requests
from bs4 import BeautifulSoup
from decimal import Decimal, InvalidOperation


class MarketYahooPrices(object):
    metal_symbol = {
        'gold': "GC=F",
        'silver': "SI=F",
    }
    currency_symbol = {
        'chfpln': 'CHFPLN=X',
        'plnchf': 'PLNCHF=X',
        'chfusd': 'CHFUSD=X',
        'usdchf': 'USDCHF=X',
        'chfeur': 'CHFEUR=X',
        'eurchf': 'EURCHF=X',
        'plnusd': 'PLNUSD=X',
        'usdpln': 'USDPLN=X',
        'plneur': 'PLNEUR=X',
        'eurpln': 'EURPLN=X',
        'eurusd': 'EURUSD=X',
        'usdeur': 'USDEUR=X',
    }

    def __init__(self, url_metals='https://in.finance.yahoo.com/commodities'):
        self.url_metals = url_metals
        self.url_host_currencies = 'https://finance.yahoo.com/quote/'
        self.url_query_currencies = '?&.tsrc=fin-srch'

    def fetch_metal_market_prices(self):
        data = {}

        try:
            page = requests.get(self.url_metals)
        except requests.exceptions.ConnectionError as e:
            print(e)
            return None

        soup = BeautifulSoup(page.content, 'html.parser')

        try:
            table_headers = soup.find('thead')
            table_body = soup.find('tbody')

            header_row = table_headers.find('tr')

            fileds_dict = {col[1].text: col[0] for col in enumerate(header_row.find_all('th'))}

            gold_record = table_body.find(class_="data-row{}".format(self.metal_symbol['gold']))
            silver_record = table_body.find(class_="data-row{}".format(self.metal_symbol['silver']))

            gold_items = gold_record.find_all('td')
            silver_items = silver_record.find_all('td')

            gold_price = Decimal(gold_items[fileds_dict['Last price']].get_text().replace(",", ""))
            silver_price = Decimal(silver_items[fileds_dict['Last price']].get_text().replace(",", ""))
        except (AttributeError, KeyError, IndexError, InvalidOperation) as e:
            print(e)
            return None

        if gold_price == 0 or silver_price == 0:
            return None

        data['gold'] = gold_price
        data['silver'] = silver_price

        return data

    def fetch_currencies_market_prices(self):
        data = {}
        for q in self.currency_symbol.values():
            try:
                page = requests.get(self.url_host_currencies + q + self.url_query_currencies)
            except requests.exceptions.ConnectionError as e:
                print(e)
                return None
            soup = BeautifulSoup(page.content, 'html.parser')
            try:
                value = Decimal(soup.find_all('span')[6].text)
                data[q[:6]] = value
            except (AttributeError, KeyError, IndexError, InvalidOperation) as e:
                print(e)
                return None
        return data
