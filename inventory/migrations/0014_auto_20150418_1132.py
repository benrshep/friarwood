# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_remove_wine_sage_ref'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appellation',
            options={'ordering': ('my_order',)},
        ),
        migrations.AlterModelOptions(
            name='employee',
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
            name='retailwine',
            options={},
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
            name='wholesalewine',
            options={},
        ),
    ]
