from inventory.models import Wine
import csv


with open('retail.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	writer.writerow([
	    	'Short Name',
	    	'sku',
	    	'price'
	    ])
		
	for wine in Wine.objects.filter(retail=True):
		writer.writerow([
			wine.short_name,
			wine.product_code,
			wine.retail_price
		])