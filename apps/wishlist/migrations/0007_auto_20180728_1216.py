# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-28 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0006_auto_20180728_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='user',
            field=models.ManyToManyField(to='wishlist.User'),
        ),
    ]
