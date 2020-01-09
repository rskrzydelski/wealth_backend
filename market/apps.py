from django.apps import AppConfig

from .fetch_yahoo import YahooMarketPrices
from django.contrib.auth.signals import user_logged_in


class MarketConfig(AppConfig):
    name = 'market'

    def ready(self):
        user_logged_in.connect(self.start_marker_attack)

    def start_marker_attack(self, sender, user, request, **kwargs):
        yahoo_th = YahooMarketPrices(1, user.my_currency)
        yahoo_th.start()
