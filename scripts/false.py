from inventory.models import Wine, Producer, Size

def run():
	
	for wine in Wine.objects.all():
		prod = wine.producer
		prod.name = prod.name.title()
		prod.save()


		'''
		wine.retail = False
		wine.wholesale = False
		wine.save()
		'''