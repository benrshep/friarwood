# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20150416_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appellation',
            name='country',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='wine',
            name='wine',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
