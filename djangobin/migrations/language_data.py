# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-20 19:42
from __future__ import unicode_literals

from django.db import migrations

LANGUAGES =[
	{
		'name':'Bash',
		'lang_code':'bash',
		'slug':'bash',
		'mime':'application/x-sh',
		'file_extension':'.sh'
	},
	{
		'name':'C',
		'lang_code':'c',
		'slug':'c',
		'mime':'text/x-chdr',
		'file_extension':'.c'
	},
	{
		'name':'C#',
		'lang_code':'c#',
		'slug':'c-sharp',
		'mime':'text/plain',
		'file_extension':'.aspx,'
	},
	{
		'name':'C++',
		'lang_code':'c++',
		'slug':'cpp',
		'mime':'text/x-c++hdr',
		'file_extension':'.cpp'
	}
]

#forward function
def add_languages(apps, schema_editor):
	Language = apps.get_model('djangobin', 'Language')

	for lang in LANGUAGES:
		l = Language.objects.get_or_create(
			name = lang['name'],
			lang_code = lang['lang_code'],
			slug =lang['slug'],
			mime = lang['mime'],
			file_extension = lang['file_extension']
		)

		print(l)

#backward function
def remove_languages(apps, schema_editor):
	Language = apps.get_model('djangobin','Language')

	for lang in LANGUAGES:
		l = Language.objects.get(
			lang_code=lang['lang_code']
		)


class Migration(migrations.Migration):

    dependencies = [
        ('djangobin', '0010_auto_20190120_1907'),
    ]

    operations = [
    	migrations.RunPython(
    		add_languages,
    		remove_languages
    	)
    ]