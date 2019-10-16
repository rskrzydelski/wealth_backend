from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Metal, Currency, Cash
from .forms import (NewMetalForm,
                    EditMetalForm,
                    NewCurrencyForm,
                    NewCashForm,
                    )


@login_required
def metal_list(request, slug):
    metal = Metal.objects.get_metal_list(owner=request.user, name=slug)
    return render(request, 'resources/metal_list.html', context={'metal_list': metal})


@login_required
def currency_list(request, slug):
    currency = Currency.objects.get_currency_list(owner=request.user, currency=slug.upper())
    return render(request, 'resources/currency_list.html', {'currency_list': currency})


@login_required
def cash_list(request):
    cash = Cash.objects.get_cash_list(owner=request.user)
    return render(request, 'resources/cash_list.html', {'cash_list': cash})


@login_required
def metal_detail(request, pk):
    metal = get_object_or_404(Metal, pk=pk)
    return render(request, 'resources/metal_detail.html', {'metal': metal})


@login_required
def currency_detail(request, pk):
    currency = get_object_or_404(Currency, pk=pk)
    return render(request, 'resources/currency_detail.html', {'currency': currency})


@login_required
def cash_detail(request, pk):
    print("pk {}".format(pk))
    cash = get_object_or_404(Cash, pk=pk)
    return render(request, 'resources/cash_detail.html', {'cash': cash})


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
def new_currency(request):
    if request.method == 'POST':
        form = NewCurrencyForm(request.POST)
        if form.is_valid():
            currency = form.save(commit=False)
            currency.owner = request.user
            currency.save()
        return redirect('resources:currency-list', form.cleaned_data.get('bought_currency').currency)
    else:
        form = NewCurrencyForm(my_currency=(request.user.my_currency, request.user.get_my_currency_display()))
    context = {
        'form': form,
    }
    return render(request, 'resources/new_currency.html', context)


@login_required
def delete_metal(request, pk):
    res = get_object_or_404(Metal, pk=pk)
    if request.method == 'POST':
        res.delete()
        return redirect('resources:metal-list', res.name)

    context = {'res': res}

    return render(request, 'resources/confirm_delete.html', context)


@login_required
def delete_currency(request, pk):
    res = get_object_or_404(Currency, pk=pk)
    print('currency delete')
    if request.method == 'POST':
        res.delete()
        return redirect('resources:currency-list', res.bought_currency.currency)

    context = {'res': res}

    return render(request, 'resources/confirm_delete.html', context)


@login_required
def edit_metal(request, pk):
    metal = get_object_or_404(Metal, pk=pk)

    if metal:
        initial_data = {
            'bought_price': metal.bought_price,
            'date_of_bought': metal.date_of_bought,
            'name': metal.name,
            'amount': metal.amount,
            'unit': metal.unit,
            'description': metal.description,
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
            metal.description = form.cleaned_data.get('description')
            metal.save()
        return redirect('resources:metal-list', slug=metal.name)
    form = EditMetalForm(initial=initial_data)
    return render(request, 'resources/edit_resource.html', {'form': form, 'metal': metal})


@login_required
def edit_currency(request, pk):
    currency = get_object_or_404(Currency, pk=pk)

    if currency:
        initial_data = {
            'bought_price': currency.bought_price,
            'date_of_bought': currency.date_of_bought,
            'bought_currency': currency.bought_currency,
        }
    else:
        initial_data = {}

    if request.method == 'POST':
        form = NewCurrencyForm(request.POST)

        if form.is_valid():
            currency.bought_price = form.cleaned_data.get('bought_price')
            currency.date_of_bought = form.cleaned_data.get('date_of_bought')
            currency.currency = form.cleaned_data.get('bought_currency')

            currency.save()

        return redirect('resources:currency-list', form.cleaned_data.get('bought_currency').currency)
    form = NewCurrencyForm(initial=initial_data,
                           my_currency=(request.user.my_currency, request.user.get_my_currency_display()))
    return render(request, 'resources/edit_resource.html', {'form': form, 'currency': currency})


@login_required
def new_cash(request):
    if request.method == 'POST':
        form = NewCashForm(request.POST)
        if form.is_valid():
            cash = form.save(commit=False)
            cash.owner = request.user
            cash.save()
        return redirect('resources:cash-list')
    else:
        form = NewCashForm(my_currency=(request.user.my_currency, request.user.get_my_currency_display()))
    context = {
        'form': form,
    }
    return render(request, 'resources/new_cash.html', context)


@login_required
def delete_cash(request, pk):
    res = get_object_or_404(Cash, pk=pk)

    if request.method == 'POST':
        res.delete()
        return redirect('resources:cash-list')

    context = {'res': res}

    return render(request, 'resources/confirm_delete.html', context)


@login_required
def edit_cash(request, pk):
    cash = get_object_or_404(Cash, pk=pk)

    if cash:
        initial_data = {
            'save_date': cash.save_date,
            'my_cash': cash.my_cash,
        }
    else:
        initial_data = {}

    if request.method == 'POST':
        form = NewCashForm(request.POST)

        if form.is_valid():
            cash.save_date = form.cleaned_data.get('save_date')
            cash.my_cash = form.cleaned_data.get('my_cash')

            cash.save()

        return redirect('resources:cash-list')
    form = NewCashForm(initial=initial_data,
                       my_currency=(request.user.my_currency, request.user.get_my_currency_display()))

    return render(request, 'resources/edit_resource.html', {'form': form})
