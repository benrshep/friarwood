# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20150418_0959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wine',
            options={'ordering': ('my_order',)},
        ),
        migrations.RemoveField(
            model_name='wine',
            name='cost_price_s',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='retail_price_s',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='w_cost_price_s',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='wholesale_price_s',
        ),
        migrations.AlterField(
            model_name='wine',
            name='cost_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='wine',
            name='retail_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='wine',
            name='wholesale_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
    ]
