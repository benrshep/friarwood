from inventory.models import Wine, Producer, Size

def run():
	
	for wine in Wine.objects.all():
		fsize = wine.single_size
		
		size, created = Size.objects.get_or_create(size=fsize)
		size.save()
		wine.size = size
		wine.save()
		