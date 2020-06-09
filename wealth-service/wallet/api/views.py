from decimal import Decimal
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import MetalWalletSerializer, CashWalletSerializer, WalletSerializer
from ..wallet import Wallet, MetalWalletData, CashWalletData, WalletData
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


@api_view(['GET'])
def cash_wallet(request):
    wallet = Wallet(owner=request.user)
    my_cash = wallet.get_all_my_cash()
    instance = CashWalletData(my_currency=request.user.my_currency, cash=my_cash)
    serializer = CashWalletSerializer(instance)
    return Response(serializer.data)


@api_view(['GET'])
def wallet(request):
    title = 'Summary of all assets value'
    wallet = Wallet(owner=request.user)

    metal_value = wallet.get_all_metals_value()
    my_cash = wallet.get_all_my_cash()
    my_fortune = metal_value + my_cash
    if metal_value is None:
        title = "Market data is not available"
        my_fortune = Decimal(0)
    instance = WalletData(title=title, my_fortune=my_fortune)
    serializer = WalletSerializer(instance)
    return Response(serializer.data)
