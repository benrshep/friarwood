# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appellation',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='pricegroup',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='producer',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='varietal',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
