from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


from .serializers import MetalWalletSerializer, CashWalletSerializer, CurrencyWalletSerializer, WalletSerializer
from ..aggregators import Aggregator, MetalWalletData, CashWalletData, CurrencyWalletData, WalletData


@api_view(['GET'])
def metal_aggregator(request, slug=None):
    aggregator = Aggregator(owner=request.user)

    value = aggregator.view_get_metal_value(name=slug)
    cash_spend = aggregator.view_get_metal_cash_spend(name=slug)

    if slug is None:
        slug = 'All metals'

    if value is None or cash_spend is None:
        slug = 'Market data is not available'

    instance = MetalWalletData(name=slug,
                               currency=request.user.my_currency,
                               total_cash=value,
                               total_cash_spend=cash_spend,
                               profit=value - cash_spend,)
    serializer = MetalWalletSerializer(instance)
    return Response(serializer.data)


@api_view(['GET'])
def cash_aggregator(request):
    aggregator = Aggregator(owner=request.user)
    my_cash = aggregator.view_get_my_cash()
    instance = CashWalletData(my_currency=request.user.my_currency,
                                cash=my_cash)
    serializer = CashWalletSerializer(instance)
    return Response(serializer.data)


@api_view(['GET'])
def currency_aggregator(request, slug=None):
    aggregator = Aggregator(owner=request.user)
    total_value = aggregator.view_get_currency_value(name=slug)

    if slug is None:
        slug = 'All currences'

    if total_value is None:
        slug = 'Market data is not available'

    instance = CurrencyWalletData(currency_name=slug,
                                  total_value=total_value)
    serializer = CurrencyWalletSerializer(instance)
    return Response(serializer.data)


@api_view(['GET'])
def wallet_aggregator(request):
    title = 'Summary of my all assets in my currency'
    aggregator = Aggregator(owner=request.user)

    total_metal_cash = aggregator.view_get_metal_value(name=None)
    my_cash = aggregator.view_get_my_cash()
    currency_value = aggregator.view_get_currency_value(name=None)

    if total_metal_cash is None or my_cash is None or currency_value is None:
        title = 'Market data is not available'
        my_fortune = None
    else:
        my_fortune = total_metal_cash + my_cash + currency_value

    instance = WalletData(title=title, my_fortune=my_fortune)
    serializer = WalletSerializer(instance)

    return Response(serializer.data)
