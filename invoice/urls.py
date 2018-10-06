"""
invoice URL Configuration
"""
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

from invoice import views

app_name = 'invoice'
urlpatterns = [
    re_path(r'^product/$', views.ProductList.as_view()),
    re_path(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    re_path(r'^customer/$', views.CustomerList.as_view()),
    re_path(r'^customer/(?P<pk>[0-9]+)/$', views.CustomerDetail.as_view()),
    re_path(r'^availableproduct/$', views.AvailableProductList.as_view()),
    re_path(r'^availableproduct/(?P<pk>[0-9]+)/$', views.AvailableProductDetail.as_view()),
    re_path(r'^order/$', views.OrderList.as_view()),
    re_path(r'^order/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view()),
    re_path(r'^orderdetail/$', views.OrderDetailList.as_view()),
    re_path(r'^orderdetail/(?P<pk>[0-9]+)/$', views.OrderDetailDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
