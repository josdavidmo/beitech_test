"""
invoice URL Configuration
"""
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

from invoice import views

app_name = 'invoice'
urlpatterns = [
    re_path(r'^order/$', views.OrderList.as_view()),
    re_path(r'^customer/$', views.CustomerList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
