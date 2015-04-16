import csv
from inventory.models import Wine, Producer
import re

def run():
	cnt = 0
	for wine in Wine.objects.all():

		producer, created = Producer.objects.get_or_create(name=wine.short_name)
		producer.save()
		wine.producer = producer
		wine.save()
	print('Complete')
