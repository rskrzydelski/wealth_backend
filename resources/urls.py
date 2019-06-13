from django.urls import path, include
from .views import resource_view

urlpatterns = [
    path('', resource_view, name='resource')
]