from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..market_data import MarketData


@api_view(['GET'])
def get_market_prices(request):
    gold_price = MarketData.get_reource_price('gold')
    silver_price = MarketData.get_reource_price('silver')

    return Response(
        {
          'Gold': gold_price,
          'Silver': silver_price
        }
    )