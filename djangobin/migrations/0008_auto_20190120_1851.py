# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-20 18:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangobin.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djangobin', '0007_auto_20190120_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='default_expiration',
            field=models.CharField(choices=[(b'never', b'Never'), (b'1 week', b'1 week'), (b'1 month', b'1 month'), (b'6 month', b'6 month'), (b'1 year', b'1 year')], default=b'never', max_length=10),
        ),
        migrations.AddField(
            model_name='author',
            name='default_exposure',
            field=models.CharField(choices=[(b'public', b'Public'), (b'unlisted', b'Unlisted'), (b'private', b'Private')], default=b'public', max_length=10),
        ),
        migrations.AddField(
            model_name='author',
            name='default_language',
            field=models.ForeignKey(default=djangobin.models.get_default_language, on_delete=django.db.models.deletion.CASCADE, to='djangobin.Language'),
        ),
        migrations.AddField(
            model_name='author',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='author',
            unique_together=set([]),
        ),
    ]
