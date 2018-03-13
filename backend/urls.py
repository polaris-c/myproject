#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
# from .views import add_book, show_books
import backend.views

urlpatterns = [
    url(r'add_book$', backend.views.add_book, ),
    url(r'show_books$', backend.views.show_books, ),
    # url(r'add_book$', add_book, ),
    # url(r'show_books$', show_books, ),
]

print('*** backend/urls is running! 中文测试***')
