import requests


class MarketTavexPrices(object):
    gold_url = "https://charts.tavex.eu/render.php?symbol=XAU&currency=PLN&period=P1D&isCandle=0&isCurrency=0&timezone=Europe%2FWarsaw"
    silver_url = "https://charts.tavex.eu/render.php?symbol=XAG&currency=PLN&period=P1D&isCandle=0&isCurrency=0&timezone=Europe%2FWarsaw"

    def __init__(self):
        pass

    @staticmethod
    def _get(url):
        response = requests.get(url)

        if response.status_code != 200:
            return None

        results = response.json().get('results')

        if not results:
            return None

        return results[-1]["c"]

    def get_gold_price(self):
        return self._get(self.gold_url)

    def get_silver_price(self):
        return self._get(self.silver_url)
