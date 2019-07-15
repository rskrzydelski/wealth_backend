from django.shortcuts import render, get_object_or_404
from .models import Metal


def wallet_view(request):
    try:
        crt_price = Metal.objects.filter(name='Ag')[0].current_price
    except IndexError:
        crt_price = 0

    silver_group = Metal(name='Ag', unit='oz', current_price=crt_price)

    try:
        crt_price = Metal.objects.filter(name='Au')[0].current_price
    except IndexError:
        crt_price = 0

    gold_group = Metal(name='Au', unit='oz', current_price=crt_price)

    for silver in Metal.objects.filter(name='Ag'):
        silver_group.amount += silver.amount

    for gold in Metal.objects.filter(name='Au'):
        gold_group.amount += gold.amount

    context = {
        'silver': silver_group,
        'gold': gold_group,
    }
    return render(request, 'resources/wallet.html', context)



