# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-20 19:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djangobin', '0009_auto_20190120_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='author',
        ),
        migrations.AddField(
            model_name='snippet',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]