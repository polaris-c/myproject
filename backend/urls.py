#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from .views import add_book, show_books

urlpatterns = [
    # url(r'add_book$', views.add_book, ),
    # url(r'show_books$', views.show_books, ),
    url(r'add_book$', add_book, ),
    url(r'show_books$', show_books, ),
]

print('*** backend/urls is running! 中文测试***')
