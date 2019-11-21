from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import MetalWalletSerializer
from ..aggregators import Aggregator, MetalWalletData
from resources.models import Metal


@api_view(['GET'])
def metal_aggregator(request, slug=None):
    aggregator = Aggregator(owner=request.user)

    total_cash = aggregator.get_current_metal_value(name=slug)
    total_cash_spend = aggregator.get_metal_cash_spend(name=slug)

    if total_cash is None or total_cash_spend is None:
        return Response(status.HTTP_404_NOT_FOUND)

    if slug is None:
        slug = 'All metals'
    instance = MetalWalletData(name=slug,
                               currency=request.user.my_currency,
                               total_cash=total_cash,
                               total_cash_spend=total_cash_spend,
                               profit=total_cash - total_cash_spend,)
    serializer = MetalWalletSerializer(instance)
    return Response(serializer.data)

