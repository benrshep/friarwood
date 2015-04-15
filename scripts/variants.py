import csv
from inventory.models import Wine, WineVariant
import re

def run():
	

	for wine in Wine.objects.all():

		variant = WineVariant.objects.create(
			wine = wine,
			single_size=wine.single_size,
			sku = wine.sku,
			product_code = wine.product_code,
			l_win = wine.l_win,
			sage_name = wine.sage_name,
			note = wine.note,

			stocked = wine.stocked,
			stock_bin = wine.stock_bin,

			octavian_ref = wine.octavian_ref,
			lcb_ref = wine.lcb_ref,
			sage_ref = wine.sage_ref,

			w_cost_price_s = wine.w_cost_price_s,
			cost_price_s = wine.cost_price_s,
			cost_price = wine.cost_price,

			retail_price_s = wine.retail_price_s,
			retail_price = wine.retail_price,

			wholesale_price_s = wine.wholesale_price_s,
			wholesale_price = wine.wholesale_price,
		)
		variant.save()