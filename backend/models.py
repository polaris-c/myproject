#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)
    # book_price = models.IntegerField()

    def  __str__(self):
        return self.book_name

print('*** backend/models is running! 中文测试***')
