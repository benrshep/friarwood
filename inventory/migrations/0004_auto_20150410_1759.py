# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_wine_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='single_size',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
