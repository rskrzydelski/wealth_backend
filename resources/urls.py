from django.urls import path, re_path, include
from .views import wallet_view


urlpatterns = [
    path('wallet/', wallet_view, name='wallet'),
]
