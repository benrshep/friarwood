# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_appellation_wine_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appellation',
            old_name='wine_list',
            new_name='retail_list',
        ),
        migrations.AddField(
            model_name='appellation',
            name='wholesale_list',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
