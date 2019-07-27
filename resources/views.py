from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Metal
from .forms import NewMetalForm, EditMetalForm


@login_required
def gold_list_view(request):
    gold = Metal.objects.filter(name='Au')
    return render(request, 'resources/gold_list.html', context={'gold_list': gold})


@login_required
def silver_list_view(request):
    silver = Metal.objects.filter(name='Ag')
    return render(request, 'resources/silver_list.html', context={'silver_list': silver})


@login_required
def new_metal(request, slug):
    if request.method == 'POST':
        form = NewMetalForm(request.POST)
        if form.is_valid():

            if slug == 'silver':
                name = 'Ag'
            else:
                name = 'Au'

            Metal.objects.create(current_price=form.cleaned_data.get('current_price'),
                                 bought_price=form.cleaned_data.get('bought_price'),
                                 date_of_bought=form.cleaned_data.get('date_of_bought'),
                                 name=name,
                                 amount=form.cleaned_data.get('amount'),
                                 unit=form.cleaned_data.get('unit'))

        return redirect('resources:{}-list'.format(slug))
    else:
        form = NewMetalForm()

    context = {
        'form': form,
        'name': slug,
    }
    return render(request, 'resources/new_metal.html', context)


@login_required
def delete_metal(request, pk):
    metal = get_object_or_404(Metal, pk=pk)
    if request.method == 'POST':
        name = metal.get_name_display()
        metal.delete()
        return redirect('resources:{}-list'.format(name.lower()))

    context = {'metal': metal}

    return render(request, 'resources/confirm_delete.html', context)


@login_required
def edit_metal(request, pk):
    metal = get_object_or_404(Metal, pk=pk)

    if metal:
        initial_data = {
            'current_price': metal.current_price,
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
            metal.current_price = form.cleaned_data.get('current_price')
            metal.bought_price = form.cleaned_data.get('bought_price')
            metal.date_of_bought = form.cleaned_data.get('date_of_bought')
            metal.name = form.cleaned_data.get('name')
            metal.amount = form.cleaned_data.get('amount')
            metal.unit = form.cleaned_data.get('unit')

            metal.save()

        return redirect('resources:{}-list'.format(metal.get_name_display().lower()))
    form = EditMetalForm(initial=initial_data)
    return render(request, 'resources/edit_metal.html', {'form': form, 'metal': metal})