from django.urls import re_path
from . import views


app_name = 'wallet'
urlpatterns = [
    re_path(r'metal/$', views.metal_aggregator, name='metal-aggregate'),
    re_path(r'metal/(?P<slug>[\w-]+)/$', views.metal_aggregator, name='metal-aggregate'),
    re_path(r'cash/$', views.cash_aggregator, name='cash-aggregate'),
    re_path(r'currency/$', views.currency_aggregator, name='currency-aggregate'),
    re_path(r'currency/(?P<slug>[\w-]+)/$', views.currency_aggregator, name='currency-aggregate'),
]
