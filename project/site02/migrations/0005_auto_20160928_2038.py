# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-28 20:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site02', '0004_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserExtended',
            new_name='UserExtend',
        ),
    ]