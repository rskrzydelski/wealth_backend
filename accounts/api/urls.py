from django.urls import re_path
from . import views


app_name = 'accounts'
urlpatterns = [
    re_path(r'login/$', views.UserLoginAPIView.as_view(), name='login'),
    re_path(r'create/$', views.UserCreateAPIView.as_view(), name='register'),
    re_path(r'(?P<pk>\d+)/$', views.UserDetailAPIView.as_view(), name='user'),
]
