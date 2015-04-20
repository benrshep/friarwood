# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_auto_20150418_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='cost_price',
            field=models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='retail_price',
            field=models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='wholesale_price',
            field=models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True),
        ),
    ]
