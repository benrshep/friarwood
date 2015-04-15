# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20150414_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='case_type',
        ),
        migrations.AddField(
            model_name='wine',
            name='pricelist',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
