# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20150428_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appellation',
            name='country',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='region',
        ),
        migrations.AddField(
            model_name='appellation',
            name='region',
            field=models.ForeignKey(blank=True, null=True, to='inventory.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='region',
            name='country',
            field=models.CharField(null=True, max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
