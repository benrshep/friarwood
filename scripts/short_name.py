from inventory.models import Wine

def run():
	for wine in Wine.objects.all():
		if wine.short_name is '':
			wine.short_name = wine.sage_name
			wine.save()
			print(wine.sage_name)