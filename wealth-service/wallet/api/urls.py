from django.urls import path, re_path
from . import views


app_name = 'wallet'
urlpatterns = [
    # path('', views.wallet_aggregator, name='wallet-aggregate'),
    re_path(r'metals$', views.metal_wallet, name='metal-wallet'),
    re_path(r'metals/(?P<slug>[\w-]+)$', views.metal_wallet, name='metal-wallet'),
    re_path(r'metals/(?P<slug>[\w-]+)/(?P<resource_id>[^/]+)$', views.metal_wallet, name='metal-wallet'),
    # re_path(r'cash$', views.cash_aggregator, name='cash-wallet'),
    # re_path(r'currency$', views.currency_aggregator, name='currency-aggregate'),
    # re_path(r'currency/(?P<slug>[\w-]+)$', views.currency_aggregator, name='currency-aggregate'),
]

