from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from resources.models import Metal, Cash, MarketPrices


@login_required(login_url='/accounts/login/')
def home_view(request):
    market_prices = MarketPrices.load()
    total_silver = Metal.get_total_metal_oz(owner=request.user, name='Ag')
    total_gold = Metal.get_total_metal_oz(owner=request.user, name='Au')
    total_pln = Cash.get_total_cash(owner=request.user, currency='PLN')
    total_usd = Cash.get_total_cash(owner=request.user, currency='USD')
    total_eur = Cash.get_total_cash(owner=request.user, currency='EUR')
    total_chf = Cash.get_total_cash(owner=request.user, currency='CHF')

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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})