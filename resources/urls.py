from django.urls import path, re_path
from . import views

urlpatterns = [
    path('gold/', views.gold_list_view, name='gold-list'),
    path('silver/', views.silver_list_view, name='silver-list'),
    re_path(r'^new/(?P<slug>[-\w]+)/$', views.new_metal, name='new-metal'),
    re_path(r'delete/(?P<pk>\d+)/$', views.delete_metal, name='del-metal'),
    re_path(r'edit/(?P<pk>\d+)/$', views.edit_metal, name='edit-metal'),
]
