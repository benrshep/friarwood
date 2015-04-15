# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20150415_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=200)),
                ('details', models.TextField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='wine',
            name='price_group',
            field=models.ForeignKey(null=True, to='inventory.PriceGroup', blank=True),
            preserve_default=True,
        ),
    ]
