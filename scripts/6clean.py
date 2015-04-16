from inventory.models import Wine

def run():
	for wine in Wine.objects.all():
		short_lower = wine.short_name.lower()
		if '19' in short_lower:
			sep = '19'
			rest = short_lower.split(sep, 1)[0]
			print(rest)

			wine.short_name = rest.title()
			wine.save()
		if '20' in short_lower:
			sep = '20'
			rest = short_lower.split(sep, 1)[0]
			print(rest)

			wine.short_name = rest.title()
			wine.save()
		if 'half' in short_lower:
			sep = 'half'
			rest = short_lower.split(sep, 1)[0]
			print(rest)

			wine.short_name = rest.title()
			wine.save()
	print('Complete')


			