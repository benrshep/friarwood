# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20150414_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='region1',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='region2',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='region3',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='region4',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='region5',
        ),
    ]
