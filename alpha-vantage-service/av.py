import requests
import collections


Resource = collections.namedtuple('Resource', ['ticker_from', 'ticker_to', 'price'])


class AvAPI(object):
    api_token = "NC4WHGIU4ZGAGHU2"
    silverusd_url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=XAG&to_currency=USD&apikey={api_token}"
    goldusd_url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=XAU&to_currency=USD&apikey={api_token}"
    usdpln_url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=PLN&apikey={api_token}"
    usdeur_url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=EUR&apikey={api_token}"
    usdchf_url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=CHF&apikey={api_token}"

    def __init__(self):
        pass

    @staticmethod
    def _get(url):
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            print('ConnectionError')
            return None

        if response.status_code != 200:
            return None

        results = response.json().get('Realtime Currency Exchange Rate')

        if not results:
            return None

        return Resource(results['1. From_Currency Code'], results['3. To_Currency Code'], results['5. Exchange Rate'])

    def get_gold(self):
        return self._get(self.goldusd_url)

    def get_silver(self):
        return self._get(self.silverusd_url)

    def get_usdpln(self):
        return self._get(self.usdpln_url)

    def get_usdeur(self):
        return self._get(self.usdeur_url)

    def get_usdchf(self):
        return self._get(self.usdchf_url)
