from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from resources.models import Metal, Cash, MarketPrices


@login_required(login_url='/accounts/login/')
def home_view(request):
    market_prices = MarketPrices.load()
    total_silver = Metal.get_total_metal_oz(owner=request.user, name='Ag') or 0
    total_gold = Metal.get_total_metal_oz(owner=request.user, name='Au') or 0
    total_pln = Cash.get_total_cash(owner=request.user, currency='PLN') or 0
    total_usd = Cash.get_total_cash(owner=request.user, currency='USD') or 0
    total_eur = Cash.get_total_cash(owner=request.user, currency='EUR') or 0
    total_chf = Cash.get_total_cash(owner=request.user, currency='CHF') or 0

    context = {
        'total_silver': total_silver,
        'total_gold': total_gold,
        'total_zloty': total_pln,
        'total_dollar': total_usd,
        'total_euro': total_eur,
        'total_franc': total_chf,
        'market_prices': market_prices,
    }
    return render(request, 'home.html', context)
