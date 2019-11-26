from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


from .serializers import MetalWalletSerializer, CashWalletSerializer, CurrencyWalletSerializer, WalletSerializer
from ..aggregators import Aggregator, MetalWalletData, CashWalletData, CurrencyWalletData, WalletData
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


@api_view(['GET'])
def cash_aggregator(request):
    aggregator = Aggregator(owner=request.user)
    my_cash = aggregator.get_my_cash()
    instance = CashWalletData(my_currency=request.user.my_currency,
                                cash=my_cash)
    serializer = CashWalletSerializer(instance)
    return Response(serializer.data)


@api_view(['GET'])
def currency_aggregator(request, slug=None):
    aggregator = Aggregator(owner=request.user)
    total_value = aggregator.get_currency_value(name=slug)

    if total_value is None:
        return Response(status.HTTP_404_NOT_FOUND)

    if slug is None:
        slug = 'All currences'

    instance = CurrencyWalletData(currency_name=slug,
                                  total_value=total_value)
    serializer = CurrencyWalletSerializer(instance)
    return Response(serializer.data)


@api_view(['GET'])
def wallet_aggregator(request):
    aggregator = Aggregator(owner=request.user)

    total_metal_cash = aggregator.get_current_metal_value(name=None)
    my_cash = aggregator.get_my_cash()
    total_currency_cash = aggregator.get_currency_value(name=None)

    my_fortune = total_metal_cash + my_cash + total_currency_cash

    instance = WalletData(title='Summary of my all assets in my currency', my_fortune=my_fortune)
    serializer = WalletSerializer(instance)

    return Response(serializer.data)