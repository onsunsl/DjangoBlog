# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @project : DjangoBlog
# @file    : urls.py
# @time    : 2020/2/1 8:47
# @author  : GuangLin
# @version : 0.01
# @desc    :


from django.urls import path
from .views import TestView


urlpatterns = [
    path("", TestView.as_view(), name="test_api"),
]
