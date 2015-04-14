# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20150410_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wine',
            old_name='cost_price',
            new_name='cost_price_s',
        ),
        migrations.RenameField(
            model_name='wine',
            old_name='retail_price',
            new_name='retail_price_s',
        ),
        migrations.RenameField(
            model_name='wine',
            old_name='wholesale_price',
            new_name='wholesale_price_s',
        ),
    ]
