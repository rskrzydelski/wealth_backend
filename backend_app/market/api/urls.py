from django.urls import path
from . import views


app_name = 'market_fetcher'
urlpatterns = [
    path('', views.get_market_prices, name='market_fetcher-prices'),
]