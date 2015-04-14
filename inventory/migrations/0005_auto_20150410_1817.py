# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20150410_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='cost_price',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='retail_price',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='retail_price_vat',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='wholesale_price',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='wholesale_price_vat',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
    ]
