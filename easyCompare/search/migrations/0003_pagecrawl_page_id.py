# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20171027_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecrawl',
            name='page_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
