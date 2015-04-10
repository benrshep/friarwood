# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20150409_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='short_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
