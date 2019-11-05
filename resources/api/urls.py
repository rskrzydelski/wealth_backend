from django.urls import re_path
from . import views


app_name = 'resources'
urlpatterns = [
    re_path(r'metals/$', views.MetalLstCreateAPIView.as_view(), name='res-create-lst'),
    re_path(r'metals/(?P<pk>\d+)/$', views.MetalDetailAPIView.as_view(), name='res-detail'),
]
