from django.urls import path
from . import views


app_name = 'market'
urlpatterns = [
    path('', views.get_market_prices, name='market-prices'),
]