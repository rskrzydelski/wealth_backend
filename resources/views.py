from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Metal

#
# class GoldListView(generic.ListView):
#     model = Metal.objects.filter(name='Au')
#     template_name = 'resources/templates/gold_list.html'  # Default: <app_label>/<model_name>_list.html

def gold_list_view(request):
    gold = Metal.objects.filter(name='Au')

    return render(request, 'resources/gold_list.html', context={'gold_list': gold})


def silver_list_view(request):
    silver = Metal.objects.filter(name='Ag')

    return render(request, 'resources/silver_list.html', context={'silver_list': silver})

#
# class SilverListView(generic.DetailView):
#     model = Metal.objects.filter(name='Ag')
#     template_name = 'resources/templates/silver_list.html'  # Default: <app_label>/<model_name>_list.html


