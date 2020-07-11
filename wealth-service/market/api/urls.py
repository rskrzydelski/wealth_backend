from django.urls import path, re_path
from . import views


app_name = 'market'
urlpatterns = [
    path('', views.market, name='market'),
]

