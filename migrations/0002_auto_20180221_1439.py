# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-21 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionapc',
            name='section',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='submission.Section'),
        ),
    ]
