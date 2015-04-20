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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('my_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('my_order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, blank=True)),
                ('my_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('my_order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PriceGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('details', models.TextField(null=True, blank=True)),
                ('my_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('my_order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('my_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('my_order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('size', models.CharField(unique=True, max_length=200, blank=True)),
                ('name', models.CharField(max_length=200, default='None')),
                ('my_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('my_order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Varietal',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('details', models.TextField(null=True, blank=True)),
                ('my_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('my_order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('wine', models.CharField(max_length=100, blank=True)),
                ('short_name', models.CharField(max_length=100, blank=True)),
                ('full_name', models.CharField(max_length=200, blank=True)),
                ('vintage', models.CharField(max_length=50, blank=True)),
                ('searcher_details', models.NullBooleanField(default=False)),
                ('searcher_url', models.CharField(max_length=200, blank=True)),
                ('searcher_price', models.DecimalField(decimal_places=2, max_digits=6, default=0)),
                ('searcher_status', models.CharField(null=True, max_length=100, blank=True)),
                ('searcher_data', models.TextField(null=True, blank=True)),
                ('colour', models.CharField(max_length=100)),
                ('wine_type', models.CharField(max_length=100)),
                ('alcohol', models.DecimalField(decimal_places=2, max_digits=3, default=0)),
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
                ('wholesale', models.BooleanField(default=False)),
                ('pricelist', models.BooleanField(default=False)),
                ('retail', models.BooleanField(default=False)),
                ('bond_stock', models.CharField(max_length=6, blank=True, default=0)),
                ('cellar_stock', models.CharField(max_length=6, blank=True, default=0)),
                ('octavian_ref', models.CharField(null=True, max_length=100, blank=True)),
                ('lcb_ref', models.CharField(null=True, max_length=100, blank=True)),
                ('cost_price', models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=6)),
                ('retail_price', models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=6)),
                ('wholesale_price', models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=6)),
                ('my_order', models.PositiveIntegerField(default=0)),
                ('appellation', models.ForeignKey(null=True, to='inventory.Appellation', blank=True)),
                ('price_group', models.ForeignKey(null=True, to='inventory.PriceGroup', blank=True)),
                ('producer', models.ForeignKey(null=True, to='inventory.Producer', blank=True)),
                ('size', models.ForeignKey(null=True, to='inventory.Size', blank=True)),
                ('varietal', models.ForeignKey(null=True, to='inventory.Varietal', blank=True)),
            ],
            options={
                'ordering': ('my_order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RetailWine',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('inventory.wine',),
        ),
        migrations.CreateModel(
            name='WholesaleWine',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('inventory.wine',),
        ),
    ]
