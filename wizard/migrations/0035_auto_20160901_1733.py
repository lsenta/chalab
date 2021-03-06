# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0034_protocolmodel_is_ready'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocolmodel',
            name='has_registration',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='protocolmodel',
            name='ranked_submissions',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='protocol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='challenge', to='wizard.ProtocolModel'),
        ),
    ]
