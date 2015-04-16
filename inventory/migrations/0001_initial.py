# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appellation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('country', models.CharField(max_length=200, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PriceGroup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('details', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('size', models.CharField(max_length=200, unique=True, blank=True)),
                ('name', models.CharField(unique=True, max_length=200, default='None')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Varietal',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('details', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('wine', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=100, blank=True)),
                ('full_name', models.CharField(max_length=200, blank=True)),
                ('vintage', models.CharField(max_length=50, blank=True)),
                ('searcher_details', models.NullBooleanField(default=False)),
                ('searcher_url', models.CharField(max_length=200, blank=True)),
                ('searcher_price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('searcher_status', models.CharField(null=True, max_length=100, blank=True)),
                ('searcher_data', models.TextField(null=True, blank=True)),
                ('colour', models.CharField(max_length=100)),
                ('wine_type', models.CharField(max_length=100)),
                ('alcohol', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('classification', models.CharField(max_length=200)),
                ('single_size', models.CharField(max_length=50, blank=True)),
                ('note', models.TextField(null=True, blank=True)),
                ('sku', models.CharField(max_length=200, blank=True)),
                ('product_code', models.CharField(null=True, max_length=20, blank=True)),
                ('l_win', models.CharField(max_length=200, blank=True)),
                ('sage_name', models.CharField(max_length=100, blank=True)),
                ('case_size', models.IntegerField(default=0)),
                ('stocked', models.NullBooleanField()),
                ('stock_bin', models.CharField(max_length=100)),
                ('wholesale', models.BooleanField(default=True)),
                ('pricelist', models.BooleanField(default=True)),
                ('retail', models.BooleanField(default=True)),
                ('octavian_ref', models.CharField(null=True, max_length=100, blank=True)),
                ('lcb_ref', models.CharField(null=True, max_length=100, blank=True)),
                ('sage_ref', models.CharField(null=True, max_length=100, blank=True)),
                ('cost_price_s', models.CharField(null=True, max_length=100, blank=True)),
                ('w_cost_price_s', models.CharField(null=True, max_length=100, blank=True)),
                ('cost_price', models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=6)),
                ('retail_price_s', models.CharField(null=True, max_length=100, blank=True)),
                ('retail_price', models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=6)),
                ('wholesale_price_s', models.CharField(null=True, max_length=100, blank=True)),
                ('wholesale_price', models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=6)),
                ('appellation', models.ForeignKey(null=True, to='inventory.Appellation', blank=True)),
                ('price_group', models.ForeignKey(null=True, to='inventory.PriceGroup', blank=True)),
                ('producer', models.ForeignKey(null=True, to='inventory.Producer', blank=True)),
                ('size', models.ForeignKey(null=True, to='inventory.Size', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
