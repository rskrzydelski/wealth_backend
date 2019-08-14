from django.urls import path, re_path
from . import views

urlpatterns = [
    # resource lists
    re_path(r'metal/list/(?P<slug>[-\w]+)/$', views.metal_list, name='metal-list'),
    re_path(r'cash/list/(?P<slug>[-\w]+)/$', views.cash_list, name='cash-list'),
    # metal action endpoints
    re_path(r'metal/new/$', views.new_metal, name='new-metal'),
    re_path(r'metal/delete/(?P<pk>\d+)/$', views.delete_metal, name='del-metal'),
    re_path(r'metal/edit/(?P<pk>\d+)/$', views.edit_metal, name='edit-metal'),
    # cash action endpoints
    re_path(r'cash/new/$', views.new_cash, name='new-cash'),
    re_path(r'cash/delete/(?P<pk>\d+)/$', views.delete_cash, name='del-cash'),
    re_path(r'cash/edit/(?P<pk>\d+)/$', views.edit_cash, name='edit-cash'),
]
