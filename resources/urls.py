from django.urls import path
from . import views

urlpatterns = [
    path('gold/', views.gold_list_view, name='gold-list'),
    path('silver/', views.silver_list_view, name='silver-list'),
]
