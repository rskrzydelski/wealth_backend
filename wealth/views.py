from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from resources.models import Metal, Currency, MarketPrices


@login_required(login_url='/accounts/login/')
def home_view(request):
    market_prices = MarketPrices.load()
    my_currency = request.user.my_currency
    total_silver = Metal.objects.get_total_silver(owner=request.user, unit='oz')
    total_gold = Metal.objects.get_total_gold(owner=request.user, unit='oz')
    total_pln = Currency.get_total_currency(owner=request.user, currency='PLN') or 0
    total_usd = Currency.get_total_currency(owner=request.user, currency='USD') or 0
    total_eur = Currency.get_total_currency(owner=request.user, currency='EUR') or 0
    total_chf = Currency.get_total_currency(owner=request.user, currency='CHF') or 0

    context = {
        'my_currency': my_currency,
        'total_silver': total_silver,
        'total_gold': total_gold,
        'total_zloty': total_pln,
        'total_dollar': total_usd,
        'total_euro': total_eur,
        'total_franc': total_chf,
        'market_prices': market_prices,
    }
    return render(request, 'home.html', context)
