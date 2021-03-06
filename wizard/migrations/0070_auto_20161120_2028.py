# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-20 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0069_metricmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='test_ratio',
            field=models.FloatField(default=10, null=True, verbose_name='Ratio for test data (percents)'),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='train_ratio',
            field=models.FloatField(default=85, null=True, verbose_name='Ratio for train data (percents)'),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='valid_ratio',
            field=models.FloatField(default=5, null=True, verbose_name='Ratio for valid data (percents)'),
        ),
    ]
