# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-16 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangobin', '0003_auto_20190116_1822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='visits',
            new_name='hits',
        ),
    ]