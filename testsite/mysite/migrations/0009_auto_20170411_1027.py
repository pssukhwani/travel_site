# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 10:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='userid',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='users',
            name='create_at',
        ),
    ]
