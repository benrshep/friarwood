# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='region',
            field=models.ForeignKey(null=True, blank=True, to='inventory.Region'),
            preserve_default=True,
        ),
    ]
