# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_wine_w_cost_price_s'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='retail_margin',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='wholesale_margin',
        ),
    ]
