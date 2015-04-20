# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20150417_1523'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('my_order',)},
        ),
        migrations.AddField(
            model_name='employee',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
