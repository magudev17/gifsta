# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-13 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gifspool', '0002_category_site_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='gif',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gifspool.Category'),
        ),
    ]