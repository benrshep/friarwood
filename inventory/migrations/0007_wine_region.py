# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_remove_wine_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='region',
            field=models.ForeignKey(null=True, to='inventory.Region', blank=True),
            preserve_default=True,
        ),
    ]
