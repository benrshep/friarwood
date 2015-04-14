from inventory.models import Wine

def run():
	for wine in Wine.objects.all():

		'''
		if wine.cost_price_s == 'NA':
			print(wine.cost_price_s)
			wine.cost_price_s = '0'
			wine.save()
		'''

		wine.cost_price = round(float(wine.cost_price_s),2)

		wine.retail_price = round(float(wine.retail_price_s),2)


			