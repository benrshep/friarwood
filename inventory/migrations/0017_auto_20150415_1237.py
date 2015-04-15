# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_auto_20150415_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winevariant',
            name='sage_name',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='winevariant',
            name='sku',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='winevariant',
            name='stock_bin',
            field=models.CharField(null=True, max_length=100),
        ),
    ]
