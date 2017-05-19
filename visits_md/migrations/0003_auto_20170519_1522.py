# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import visits_md.validators


class Migration(migrations.Migration):

    dependencies = [
        ('visits_md', '0002_auto_20170519_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, validators=[visits_md.validators.validate_startend]),
        ),
    ]