from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Metal, Cash
from .forms import NewMetalForm, EditMetalForm, NewCashForm


@login_required
def metal_list(request, slug):
    metal = Metal.get_metal_list(owner=request.user, name=slug)
    return render(request, 'resources/metal_list.html', context={'metal_list': metal})


@login_required
def cash_list(request, slug):
    cash = Cash.get_cash_list(owner=request.user, currency=slug.upper())
    return render(request, 'resources/cash_list.html', {'cash_list': cash})


@login_required
def new_metal(request):
    if request.method == 'POST':
        form = NewMetalForm(request.POST)
        if form.is_valid():
            metal = form.save(commit=False)
            metal.owner = request.user
            metal.save()
        return redirect('resources:metal-list', form.cleaned_data.get('name'))
    else:
        form = NewMetalForm()

    context = {
        'form': form,
    }
    return render(request, 'resources/new_metal.html', context)


@login_required
def new_cash(request):
    if request.method == 'POST':
        form = NewCashForm(request.POST)
        if form.is_valid():
            cash = form.save(commit=False)
            cash.owner = request.user
            cash.save()
        return redirect('resources:cash-list', form.cleaned_data.get('currency'))
    else:
        form = NewCashForm()
    context = {
        'form': form,
    }
    return render(request, 'resources/new_cash.html', context)


@login_required
def delete_metal(request, pk):
    res = get_object_or_404(Metal, pk=pk)
    if request.method == 'POST':
        res.delete()
        return redirect('resources:metal-list', res.name)

    context = {'res': res}

    return render(request, 'resources/confirm_delete.html', context)


@login_required
def delete_cash(request, pk):
    res = get_object_or_404(Cash, pk=pk)
    if request.method == 'POST':
        res.delete()
        return redirect('resources:cash-list', res.currency.lower())

    context = {'res': res}

    return render(request, 'resources/confirm_delete.html', context)


@login_required
def edit_metal(request, pk):
    metal = get_object_or_404(Metal, pk=pk)

    if metal:
        initial_data = {
            'bought_price': metal.bought_price,
            'date_of_bought': metal.date_of_bought,
            'amount': metal.amount,
            'unit': metal.unit,
            'name': metal.name,
        }
    else:
        initial_data = {}

    if request.method == 'POST':
        form = EditMetalForm(request.POST)

        if form.is_valid():
            metal.bought_price = form.cleaned_data.get('bought_price')
            metal.date_of_bought = form.cleaned_data.get('date_of_bought')
            metal.name = form.cleaned_data.get('name')
            metal.amount = form.cleaned_data.get('amount')
            metal.unit = form.cleaned_data.get('unit')

            metal.save()

        return redirect('resources:metal-list', slug=metal.name)
    form = EditMetalForm(initial=initial_data)
    return render(request, 'resources/edit_resource.html', {'form': form, 'metal': metal})


@login_required
def edit_cash(request, pk):
    cash = get_object_or_404(Cash, pk=pk)

    if cash:
        initial_data = {
            'bought_price': cash.bought_price,
            'date_of_bought': cash.date_of_bought,
            'amount': cash.amount,
            'my_currency': cash.my_currency,
            'currency': cash.currency,
        }
    else:
        initial_data = {}

    if request.method == 'POST':
        form = NewCashForm(request.POST)

        if form.is_valid():
            cash.bought_price = form.cleaned_data.get('bought_price')
            cash.date_of_bought = form.cleaned_data.get('date_of_bought')
            cash.amount = form.cleaned_data.get('amount')
            cash.my_currency = form.cleaned_data.get('my_currency')
            cash.currency = form.cleaned_data.get('currency')

            cash.save()

        return redirect('resources:cash-list', form.cleaned_data.get('currency'))
    form = NewCashForm(initial=initial_data)
    return render(request, 'resources/edit_resource.html', {'form': form, 'cash': cash})
