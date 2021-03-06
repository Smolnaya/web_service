# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2021-10-07 09:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('author', models.CharField(default='', max_length=100)),
                ('text', models.TextField(default='')),
                ('publication_date', models.DateField(default=datetime.date.today)),
                ('source', models.CharField(default='', max_length=50, null=True)),
                ('tags', models.CharField(default='', max_length=50, null=True)),
            ],
        ),
    ]
