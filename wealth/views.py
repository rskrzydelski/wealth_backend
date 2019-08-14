from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from resources.models import Metal, Cash, MarketPrices


@login_required(login_url='/accounts/login/')
def home_view(request):
    prices = MarketPrices.load()
    silver_group = Metal(owner=request.user, name='Ag', unit='oz')
    gold_group = Metal(owner=request.user, name='Au', unit='oz')
    zloty_group = Cash(owner=request.user, currency='PLN')
    dollar_group = Cash(owner=request.user, currency='USD')
    euro_group = Cash(owner=request.user, currency='EUR')
    franc_group = Cash(owner=request.user, currency='CHF')

    # metal groups
    for silver in Metal.objects.filter(owner=request.user, name='Ag'):
        silver_group.amount += silver.amount

    for gold in Metal.objects.filter(owner=request.user, name='Au'):
        gold_group.amount += gold.amount

    # cash groups
    for zloty in Cash.objects.filter(owner=request.user, currency='PLN'):
        zloty_group.amount += zloty.amount

    for dollar in Cash.objects.filter(owner=request.user, currency='USD'):
        dollar_group.amount += dollar.amount

    for euro in Cash.objects.filter(owner=request.user, currency='EUR'):
        euro_group.amount += euro.amount

    for franc in Cash.objects.filter(owner=request.user, currency='CHF'):
        franc_group.amount += franc.amount

    context = {
        'silver': silver_group,
        'gold': gold_group,
        'zloty': zloty_group,
        'dollar': dollar_group,
        'euro': euro_group,
        'franc': franc_group,
        'market_prices': prices,
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