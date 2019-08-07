from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from resources.models import Metal


@login_required(login_url='/accounts/login/')
def home_view(request):
    try:
        crt_price = Metal.objects.filter(owner=request.user, name='Ag')[0].current_price
    except IndexError:
        crt_price = 0

    silver_group = Metal(owner=request.user, name='Ag', unit='oz', current_price=crt_price)

    try:
        crt_price = Metal.objects.filter(owner=request.user, name='Au')[0].current_price
    except IndexError:
        crt_price = 0

    gold_group = Metal(owner=request.user, name='Au', unit='oz', current_price=crt_price)

    for silver in Metal.objects.filter(owner=request.user, name='Ag'):
        silver_group.amount += silver.amount

    for gold in Metal.objects.filter(owner=request.user, name='Au'):
        gold_group.amount += gold.amount

    context = {
        'silver': silver_group,
        'gold': gold_group,
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