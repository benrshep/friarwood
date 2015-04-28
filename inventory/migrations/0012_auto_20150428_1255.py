# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20150428_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='country',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
