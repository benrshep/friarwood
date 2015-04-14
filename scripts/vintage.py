import csv
from inventory.models import Wine
import re

def run():
	for wine in Wine.objects.all():
		nums = re.findall(r'\d+', wine.sage_name)
		if 'NV' in wine.sage_name:
			wine.vintage = 'NV'
			wine.save()
		else:
			try:
				wine.vintage = nums[0]
				wine.save()
				#print(nums)
			except:
				print(nums)	