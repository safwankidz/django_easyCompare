# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 15:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20171029_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchitem',
            name='page',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='search.PageCrawl'),
            preserve_default=False,
        ),
    ]
