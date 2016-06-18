# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-18 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_vision'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vision',
        ),
        migrations.RemoveField(
            model_name='club',
            name='about',
        ),
        migrations.RemoveField(
            model_name='club',
            name='vision',
        ),
        migrations.AddField(
            model_name='subtopic',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
