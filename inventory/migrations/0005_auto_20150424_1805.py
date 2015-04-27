# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_wine_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='colour',
            field=models.CharField(max_length=10, choices=[('R', 'Red'), ('W', 'White'), ('Ro', 'Rose')]),
        ),
    ]
