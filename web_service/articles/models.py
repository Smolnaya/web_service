from __future__ import unicode_literals

import datetime
from django.db import models


class Article(models.Model):
    GAMES = 'Игры'
    OS = 'ОС'
    CATEGORIES = [
        (GAMES, 'Игры'),
        (OS, 'ОС')
    ]
    title = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=100, default='')
    text = models.TextField(max_length=None, default='')
    publication_date = models.DateField(default=datetime.date.today)
    source = models.CharField(max_length=50, null=True, default='', blank=True)
    tags = models.CharField(max_length=50, null=True, default='', blank=True)
    category = models.CharField(max_length=100, choices=CATEGORIES, default='', blank=True)

