# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20150417_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceListWine',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('inventory.wine',),
        ),
        migrations.AddField(
            model_name='wine',
            name='bond_stock',
            field=models.CharField(default=0, blank=True, max_length=6),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='wine',
            name='cellar_stock',
            field=models.CharField(default=0, blank=True, max_length=6),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='wine',
            name='found',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
