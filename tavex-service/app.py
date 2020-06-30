import time
from tavex import MarketTavexPrices
import mongomarket


gold_spread = 0.96
silver_spread = 0.85


def tavex_market():
    tavex = MarketTavexPrices()

    while True:
        gold999oz = tavex.get_gold_price()
        silver999oz = tavex.get_silver_price()

        if gold999oz:
            gold999g = (gold999oz / 31.1) * gold_spread
            gold999kg = (gold999oz / 31.1) * 1000
            gold585oz = (gold999oz * 0.585) * gold_spread
            gold585g = (gold999g * 0.585) * gold_spread
            gold333oz = (gold999oz * 0.333) * gold_spread
            gold333g = (gold999g * 0.333) * gold_spread

            mongomarket.set_metal_price('gold999oz', gold999oz, 'PLN', 'oz')
            mongomarket.set_metal_price('gold999g', gold999g, 'PLN', 'g')
            mongomarket.set_metal_price('gold999kg', gold999kg, 'PLN', 'kg')

            mongomarket.set_metal_price('gold585oz', gold585oz, 'PLN', 'oz')
            mongomarket.set_metal_price('gold585g', gold585g, 'PLN', 'g')
            mongomarket.set_metal_price('gold333oz', gold333oz, 'PLN', 'oz')
            mongomarket.set_metal_price('gold333g', gold333g, 'PLN', 'g')

        if silver999oz:
            silver999g = (silver999oz / 31.1) * silver_spread
            silver800oz = (silver999oz * 0.800) * silver_spread
            silver800g = (silver999g * 0.800) * silver_spread

            mongomarket.set_metal_price('silver999oz', silver999oz, 'PLN', 'oz')
            mongomarket.set_metal_price('silver999g', silver999g, 'PLN', 'g')
            mongomarket.set_metal_price('silver800oz', silver800oz, 'PLN', 'oz')
            mongomarket.set_metal_price('silver800g', silver800g, 'PLN', 'g')

        time.sleep(60)


if __name__ == '__main__':
    tavex_market()
