# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20150415_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='varietal',
            field=models.ForeignKey(null=True, to='inventory.Varietal', blank=True),
            preserve_default=True,
        ),
    ]
