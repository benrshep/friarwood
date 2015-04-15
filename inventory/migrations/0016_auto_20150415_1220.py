# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0015_auto_20150415_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='WineVariant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('single_size', models.CharField(blank=True, max_length=50)),
                ('sku', models.CharField(blank=True, max_length=200)),
                ('product_code', models.CharField(blank=True, null=True, max_length=20)),
                ('l_win', models.CharField(blank=True, max_length=200)),
                ('sage_name', models.CharField(blank=True, max_length=100)),
                ('note', models.TextField(blank=True, null=True)),
                ('case_size', models.IntegerField(default=0)),
                ('stocked', models.NullBooleanField()),
                ('stock_bin', models.CharField(max_length=100)),
                ('wholesale', models.BooleanField(default=True)),
                ('pricelist', models.BooleanField(default=True)),
                ('retail', models.BooleanField(default=True)),
                ('octavian_ref', models.CharField(blank=True, null=True, max_length=100)),
                ('lcb_ref', models.CharField(blank=True, null=True, max_length=100)),
                ('sage_ref', models.CharField(blank=True, null=True, max_length=100)),
                ('w_cost_price_s', models.CharField(blank=True, null=True, max_length=100)),
                ('cost_price_s', models.CharField(blank=True, null=True, max_length=100)),
                ('cost_price', models.DecimalField(blank=True, max_digits=6, decimal_places=2, null=True)),
                ('retail_price_s', models.CharField(blank=True, null=True, max_length=100)),
                ('retail_price', models.DecimalField(blank=True, max_digits=6, decimal_places=2, null=True)),
                ('wholesale_price_s', models.CharField(blank=True, null=True, max_length=100)),
                ('wholesale_price', models.DecimalField(blank=True, max_digits=6, decimal_places=2, null=True)),
                ('wine', models.ForeignKey(to='inventory.Wine')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='winevariation',
            name='wine',
        ),
        migrations.DeleteModel(
            name='WineVariation',
        ),
    ]
