# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_wine_varietal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='pricelist',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='wine',
            name='retail',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='wine',
            name='wholesale',
            field=models.BooleanField(default=False),
        ),
    ]
