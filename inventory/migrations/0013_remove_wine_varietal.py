# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20150415_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='varietal',
        ),
    ]
