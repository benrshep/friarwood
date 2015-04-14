# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20150411_0725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='retail_price_vat',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='wholesale_price_vat',
        ),
        migrations.AddField(
            model_name='wine',
            name='cost_price',
            field=models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='wine',
            name='retail_price',
            field=models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='wine',
            name='wholesale_price',
            field=models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='wine',
            name='sage_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
