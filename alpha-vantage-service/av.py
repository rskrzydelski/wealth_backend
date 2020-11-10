import time
import requests
import collections


Resource = collections.namedtuple('Resource', ['ticker_from', 'ticker_to', 'price'])


class AvAPI(object):
    api_token = "NC4WHGIU4ZGAGHU2"
    URL = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_c}&to_currency={to_c}&apikey={api_token}"

    def __init__(self):
        pass

    def _get(self, from_currency, to_currency):
        try:
            response = requests.get(self.URL.format(from_c=from_currency, to_c=to_currency, api_token=self.api_token))
        except requests.exceptions.ConnectionError:
            print('ConnectionError')
            return None

        if response.status_code != 200:
            return None

        results = response.json().get('Realtime Currency Exchange Rate')

        if not results:
            return None

        return Resource(results['1. From_Currency Code'], results['3. To_Currency Code'], results['5. Exchange Rate'])

    def get_resource(self, from_currency="", to_currency=""):
        time.sleep(5)
        return self._get(from_currency, to_currency)
