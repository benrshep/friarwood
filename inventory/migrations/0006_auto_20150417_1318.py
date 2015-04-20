# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20150417_1027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appellation',
            options={'ordering': ('my_order',)},
        ),
        migrations.AlterModelOptions(
            name='pricegroup',
            options={'ordering': ('my_order',)},
        ),
        migrations.AlterModelOptions(
            name='producer',
            options={'ordering': ('my_order',)},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'ordering': ('my_order',)},
        ),
        migrations.AlterModelOptions(
            name='varietal',
            options={'ordering': ('my_order',)},
        ),
        migrations.AlterModelOptions(
            name='wine',
            options={'ordering': ('my_order',)},
        ),
        migrations.AddField(
            model_name='appellation',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pricegroup',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producer',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='size',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='varietal',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='wine',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
