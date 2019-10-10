from django.urls import path, re_path
from . import views


app_name = 'resources'
urlpatterns = [
    # resource lists
    re_path(r'metal/list/(?P<slug>[-\w]+)/$', views.metal_list, name='metal-list'),
    re_path(r'currency/list/(?P<slug>[-\w]+)/$', views.currency_list, name='currency-list'),
    # resources details
    re_path(r'metal/(?P<pk>\d+)/$', views.metal_detail, name='metal-detail'),
    re_path(r'currency/(?P<pk>\d+)/$', views.currency_detail, name='currency-detail'),
    # metal action endpoints
    re_path(r'metal/new/$', views.new_metal, name='new-metal'),
    re_path(r'metal/delete/(?P<pk>\d+)/$', views.delete_metal, name='del-metal'),
    re_path(r'metal/edit/(?P<pk>\d+)/$', views.edit_metal, name='edit-metal'),
    # currency action endpoints
    re_path(r'currency/new/$', views.new_currency, name='new-currency'),
    re_path(r'currency/delete/(?P<pk>\d+)/$', views.delete_currency, name='del-currency'),
    re_path(r'currency/edit/(?P<pk>\d+)/$', views.edit_currency, name='edit-currency'),
    # cash action endpoints
    # re_path(r'cash/new/$', views.new_cash, name='new-cash'),
    # re_path(r'cash/delete/(?P<pk>\d+)/$', views.delete_cash, name='del-cash'),
    # re_path(r'cash/edit/(?P<pk>\d+)/$', views.edit_cash, name='edit-cash'),
]
