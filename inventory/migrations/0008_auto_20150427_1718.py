# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_wine_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='colour',
            field=models.CharField(choices=[('R', 'Red'), ('W', 'White'), ('Ro', 'Rose')], blank=True, max_length=10),
        ),
    ]
