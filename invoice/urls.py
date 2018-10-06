"""
invoice URL Configuration
"""
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

from invoice import views

app_name = 'invoice'
urlpatterns = [
    re_path(r'^product/$', views.ProductLC.as_view()),
    re_path(r'^product/(?P<pk>[0-9]+)/$', views.ProductRUD.as_view()),
    re_path(r'^customer/$', views.CustomerLC.as_view()),
    re_path(r'^customer/(?P<pk>[0-9]+)/$', views.CustomerRUD.as_view()),
    re_path(r'^availableproduct/$', views.AvailableProductLC.as_view()),
    re_path(r'^availableproduct/(?P<pk>[0-9]+)/$', views.AvailableProductRUD.as_view()),
    re_path(r'^order/$', views.OrderLC.as_view()),
    re_path(r'^order/(?P<pk>[0-9]+)/$', views.OrderRUD.as_view()),
    re_path(r'^orderdetail/$', views.OrderDetailLC.as_view()),
    re_path(r'^orderdetail/(?P<pk>[0-9]+)/$', views.OrderDetailRUD.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
