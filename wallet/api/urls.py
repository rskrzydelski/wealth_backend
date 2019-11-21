from django.urls import re_path
from . import views


app_name = 'wallet'
urlpatterns = [
    re_path(r'metal/$', views.metal_aggregator, name='metal-aggregate'),
    re_path(r'metal/(?P<slug>[\w-]+)/$', views.metal_aggregator, name='metal-aggregate'),
]
