from django.apps import AppConfig

from .fetch_yahoo import YahooMarketPrices


class MarketConfig(AppConfig):
    name = 'market'

    def ready(self):
        yahoo_th = YahooMarketPrices(thread_id=1)
        yahoo_th.start()
