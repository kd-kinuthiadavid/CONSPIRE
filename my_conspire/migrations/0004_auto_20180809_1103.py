# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-09 08:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_conspire', '0003_auto_20180809_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_conspire.Question'),
        ),
    ]
