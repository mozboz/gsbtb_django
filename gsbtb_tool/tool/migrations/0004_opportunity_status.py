# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-01 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0003_auto_20161201_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]