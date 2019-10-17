from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from resources.models import Metal, Currency, MarketPrices, Cash


@login_required(login_url='/accounts/login/')
def home_view(request):
    market_prices = MarketPrices.load()
    my_currency = request.user.my_currency
    total_silver = Metal.objects.get_total_silver(owner=request.user, unit='oz')
    total_gold = Metal.objects.get_total_gold(owner=request.user, unit='oz')

    total_pln = Currency.objects.get_total_currency(owner=request.user,
                                                    currency='PLN') if my_currency != 'PLN' else None
    total_usd = Currency.objects.get_total_currency(owner=request.user,
                                                    currency='USD') if my_currency != 'USD' else None
    total_eur = Currency.objects.get_total_currency(owner=request.user,
                                                    currency='EUR') if my_currency != 'EUR' else None
    total_chf = Currency.objects.get_total_currency(owner=request.user,
                                                    currency='CHF') if my_currency != 'CHF' else None

    total_cash = Cash.objects.get_total_cash(owner=request.user) or 0

    context = {
        'my_currency': my_currency,
        'total_silver': total_silver,
        'total_gold': total_gold,
        'total_zloty': total_pln,
        'total_dollar': total_usd,
        'total_euro': total_eur,
        'total_franc': total_chf,
        'total_cash': total_cash,
        'market_prices': market_prices,
    }
    return render(request, 'home.html', context)
