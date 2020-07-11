from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from ..market_data import MarketData


metals = ['gold999', 'gold585', 'gold333', 'silver999', 'silver800']
units = ['oz', 'g', 'kg']


def is_query_valid(name, unit):
    if not name in metals:
        return False
    if not unit in units:
        return False
    return True


@api_view(['GET'])
def market(request):
    name = request.GET.get('name')
    unit = request.GET.get('unit')

    if is_query_valid(name, unit):
        metal_price = MarketData.get_metal_market_price(name=name, unit=unit, currency=request.user.my_currency)
        data = {'name': name, 'unit': 'oz', 'price': metal_price, 'currency': request.user.my_currency}
    else:
        data = {'error': f"please provide following query for name: {', '.join(metals)} and unit: {', '.join(units)}"}
    return Response(data)
