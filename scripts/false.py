from inventory.models import Wine, Producer, Size

def run():
	
	for wine in Wine.objects.all():

		wine.wholesale_price = 0.00
		wine.retail_price = 0.00
		wine.cost_price = 0.00
		wine.save()

		try:
			cp = ''.join(_ for _ in wine.cost_price_s if _ in ".1234567890")
			wine.cost_price = float(cp)
			wine.save()
		except:
			wine.cost_price = 0.00
			wine.save()
		
		try:
			rp = ''.join(_ for _ in wine.retail_price_s if _ in ".1234567890")
			wine.retail_price = float(rp)
			wine.save()
		except:
			wine.retail_price = 0.00
			wine.save()
		
		try:
			wp = ''.join(_ for _ in wine.wholesale_price_s if _ in ".1234567890")
			wine.wholesale_price = float(wp)
			wine.save()
		except:
			wine.wholesale_price = 0.00
			wine.save()

		'''
		#prod = wine.producer
		#prod.name = prod.name.title()
		#prod.save()
		wine.wholesale=False
		wine.save()
		'''

		'''
		wine.retail = False
		wine.wholesale = False
		wine.save()
		'''