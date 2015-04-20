# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20150417_1700'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PriceListWine',
        ),
        migrations.CreateModel(
            name='RetailWine',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name': '3. Retail Wine',
            },
            bases=('inventory.wine',),
        ),
        migrations.CreateModel(
            name='WholesaleWine',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name': '2. Wholesale Wine',
            },
            bases=('inventory.wine',),
        ),
        migrations.AlterModelOptions(
            name='appellation',
            options={'ordering': ('my_order',), 'verbose_name': '7. Appellation'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('my_order',), 'verbose_name': '5. Employee'},
        ),
        migrations.AlterModelOptions(
            name='pricegroup',
            options={'ordering': ('my_order',), 'verbose_name': '4. Price List Group'},
        ),
        migrations.AlterModelOptions(
            name='producer',
            options={'ordering': ('my_order',), 'verbose_name': '6. Producer'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'ordering': ('my_order',), 'verbose_name': '9. Size'},
        ),
        migrations.AlterModelOptions(
            name='varietal',
            options={'ordering': ('my_order',), 'verbose_name': '8. Varietal'},
        ),
        migrations.AlterModelOptions(
            name='wine',
            options={'ordering': ('my_order',), 'verbose_name': '1. Wine'},
        ),
        migrations.RemoveField(
            model_name='wine',
            name='found',
        ),
    ]
