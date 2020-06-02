from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


from .serializers import MetalWalletSerializer, CashWalletSerializer, CurrencyWalletSerializer, WalletSerializer
from ..wallet import Wallet, MetalWalletData, CashWalletData, CurrencyWalletData, WalletData
from resources.models import Metal


def validate_slug_name(slug):
    if any(slug == m[0] for m in Metal.METAL_CHOICES):
        return True
    else:
        return False


def get_metal_wallet(wallet_inst, currency, name, resource_id):
    data = {}
    data['metal_value'] = wallet_inst.get_metal_value(name=name, resource_id=resource_id)
    data['cash_spend'] = wallet_inst.get_metal_cash_spend(name=name, resource_id=resource_id)
    data['name'] = f'Metal {name} with id {resource_id}'
    data['currency'] = currency
    data['profit'] = wallet_inst.get_metal_profit(name=name, resource_id=resource_id)
    return data


def get_metals_wallet(wallet_inst, currency, name):
    data = {}
    data['metal_value'] = wallet_inst.get_metals_value(name=name)
    data['cash_spend'] = wallet_inst.get_metals_cash_spend(name=name)
    if validate_slug_name(name):
        data['name'] = f'All {name}'
    else:
        pass
    data['currency'] = currency
    data['profit'] = wallet_inst.get_metals_profit(name)
    return data


def get_all_metals_wallet(wallet_inst, currency):
    data = {}
    data['metal_value'] = wallet_inst.get_all_metals_value()
    data['cash_spend'] = wallet_inst.get_all_metals_cash_spend()
    data['name'] = 'All metals'
    data['currency'] = currency
    data['profit'] = wallet_inst.get_all_metals_profit()
    return data


@api_view(['GET'])
def metal_wallet(request, slug=None, resource_id=None):
    wallet = Wallet(owner=request.user)

    if slug and resource_id:
        data = get_metal_wallet(wallet_inst=wallet, currency=request.user.my_currency, name=slug, resource_id=resource_id)
    elif slug:
        data = get_metals_wallet(wallet_inst=wallet, currency=request.user.my_currency, name=slug)
    else:
        data = get_all_metals_wallet(wallet_inst=wallet, currency=request.user.my_currency)

    instance = MetalWalletData(**data)
    serializer = MetalWalletSerializer(instance)
    return Response(serializer.data)


# @api_view(['GET'])
# def cash_wallet(request):
#     aggregator = Aggregator(owner=request.user)
#     my_cash = aggregator.view_get_my_cash()
#     instance = CashWalletData(my_currency=request.user.my_currency,
#                                 cash=my_cash)
#     serializer = CashWalletSerializer(instance)
#     return Response(serializer.data)

#
# @api_view(['GET'])
# def currency_wallet(request, slug=None):
#     aggregator = Aggregator(owner=request.user)
#     total_value = aggregator.view_get_currency_value(name=slug)
#
#     if slug is None:
#         slug = 'All currences'
#
#     if total_value is None:
#         slug = 'Market data is not available'
#
#     instance = CurrencyWalletData(currency_name=slug,
#                                   total_value=total_value)
#     serializer = CurrencyWalletSerializer(instance)
#     return Response(serializer.data)


# @api_view(['GET'])
# def wallet_aggregator(request):
#     title = 'Summary of my all assets in my currency'
#     aggregator = Aggregator(owner=request.user)
#
#     total_metal_cash = aggregator.view_get_metal_value(name=None)
#     my_cash = aggregator.view_get_my_cash()
#     currency_value = aggregator.view_get_currency_value(name=None)
#
#     if total_metal_cash is None or my_cash is None or currency_value is None:
#         title = 'Market data is not available'
#         my_fortune = None
#     else:
#         my_fortune = total_metal_cash + my_cash + currency_value
#
#     instance = WalletData(title=title, my_fortune=my_fortune)
#     serializer = WalletSerializer(instance)
#
#     return Response(serializer.data)
