# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateTimeField(),
        ),
    ]