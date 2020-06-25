import time
from tavex import MarketTavexPrices


gold_spread = 0.96
silver_spread = 0.85

def tavex_market():

    tavex = MarketTavexPrices()

    while True:
        gold999oz = tavex.get_gold_price()
        silver999oz = tavex.get_silver_price()

        if gold999oz:
            gold999g = (gold999oz / 31.1) * gold_spread
            gold585oz = (gold999oz * 0.585) * gold_spread
            gold585g = (gold999g * 0.585) * gold_spread
            gold333oz = (gold999oz * 0.333) * gold_spread
            gold333g = (gold999g * 0.333) * gold_spread
            print(f"gold999 oz price {gold999oz}")
            print(f"gold999 g price {gold999g}")
            print(f"gold585 oz price {gold585oz}")
            print(f"gold585 g price {gold585g}")
            print(f"gold333 oz price {gold333oz}")
            print(f"gold333 g price {gold333g}")

        if silver999oz:
            silver999g = (silver999oz / 31.1) * silver_spread
            silver800oz = (silver999oz * 0.800) * silver_spread
            silver800g = (silver999g * 0.800) * silver_spread
            print(f"silver999 oz price {silver999oz}")
            print(f"silver999 g price {silver999g}")
            print(f"silver800 oz price {silver800oz}")
            print(f"silver800 g price {silver800g}")

        time.sleep(60)


if __name__ == '__main__':
    tavex_market()
