# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_wine_product_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='WineVariation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('single_size', models.CharField(max_length=50, blank=True)),
                ('sku', models.CharField(max_length=200, blank=True)),
                ('product_code', models.CharField(max_length=20, blank=True, null=True)),
                ('l_win', models.CharField(max_length=200, blank=True)),
                ('sage_name', models.CharField(max_length=100, blank=True)),
                ('note', models.TextField(null=True, blank=True)),
                ('case_size', models.IntegerField(default=0)),
                ('stocked', models.NullBooleanField()),
                ('stock_bin', models.CharField(max_length=100)),
                ('wholesale', models.BooleanField(default=True)),
                ('pricelist', models.BooleanField(default=True)),
                ('retail', models.BooleanField(default=True)),
                ('octavian_ref', models.CharField(max_length=100, blank=True, null=True)),
                ('lcb_ref', models.CharField(max_length=100, blank=True, null=True)),
                ('sage_ref', models.CharField(max_length=100, blank=True, null=True)),
                ('w_cost_price_s', models.CharField(max_length=100, blank=True, null=True)),
                ('cost_price_s', models.CharField(max_length=100, blank=True, null=True)),
                ('cost_price', models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6)),
                ('retail_price_s', models.CharField(max_length=100, blank=True, null=True)),
                ('retail_price', models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6)),
                ('wholesale_price_s', models.CharField(max_length=100, blank=True, null=True)),
                ('wholesale_price', models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6)),
                ('wine', models.ForeignKey(to='inventory.Wine')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='wine',
            name='vat',
        ),
    ]
