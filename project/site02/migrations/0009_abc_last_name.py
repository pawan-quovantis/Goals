# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-28 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site02', '0008_userextended'),
    ]

    operations = [
        migrations.AddField(
            model_name='abc',
            name='last_name',
            field=models.CharField(default='p', max_length=12),
            preserve_default=False,
        ),
    ]
