import pprint

from yahoo import MarketYahooPrices


if __name__ == '__main__':
    fetcher = MarketYahooPrices()
    currency_prices = fetcher.fetch_currencies_market_prices()
    metal_prices = fetcher.fetch_metal_market_prices()

    pprint.pprint('Metal dict {}'.format(metal_prices))
    pprint.pprint('Currency dict {}'.format(currency_prices))
