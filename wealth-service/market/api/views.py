from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..market_data import MarketData


@api_view(['GET'])
def get_market_prices(request):
    gold_price = MarketData.get_reource_price('gold')
    silver_price = MarketData.get_reource_price('silver')
    chfpln_price = MarketData.get_reource_price('CHFPLN')
    plnchf_price = MarketData.get_reource_price('PLNCHF')
    chfusd_price = MarketData.get_reource_price('CHFUSD')
    usdchf_price = MarketData.get_reource_price('USDCHF')
    chfeur_price = MarketData.get_reource_price('CHFEUR')
    eurchf_price = MarketData.get_reource_price('EURCHF')
    plnusd_price = MarketData.get_reource_price('PLNUSD')
    usdpln_price = MarketData.get_reource_price('USDPLN')
    plneur_price = MarketData.get_reource_price('PLNEUR')
    eurpln_price = MarketData.get_reource_price('EURPLN')
    eurusd_price = MarketData.get_reource_price('EURUSD')
    usdeur_price = MarketData.get_reource_price('USDEUR')

    return Response(
        {
          'gold': gold_price,
          'silver': silver_price,
          'chfpln': chfpln_price,
          'plnchf': plnchf_price,
          'chfusd': chfusd_price,
          'usdchf': usdchf_price,
          'chfeur': chfeur_price,
          'eurchf': eurchf_price,
          'plnusd': plnusd_price,
          'usdpln': usdpln_price,
          'plneur': plneur_price,
          'eurpln': eurpln_price,
          'eurusd': eurusd_price,
          'usdeur': usdeur_price,
        }
    )
