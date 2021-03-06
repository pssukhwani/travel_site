# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0021_auto_20170413_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='available_from',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='available_till',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='image',
            field=models.ImageField(upload_to=b''),
        ),
    ]
