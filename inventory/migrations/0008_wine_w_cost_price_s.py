# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20150411_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='w_cost_price_s',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
