# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20150427_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='appellation',
            name='wine_list',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
