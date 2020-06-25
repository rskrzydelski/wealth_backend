from tavex import MarketTavexPrices


if __name__ == '__main__':
    tavex = MarketTavexPrices()
    gold999 = tavex.get_gold_price()
    silver999 = tavex.get_silver_price()

    if gold999:
        print(f"write gold999 value {gold999} to mongodb ...")

    if silver999:
        print(f"write silver999 value {silver999} to mongodb ...")

