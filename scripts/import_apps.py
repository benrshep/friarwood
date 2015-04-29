from inventory.models import Wine, Producer, Size, Appellation
import csv

def run():
	
	#for wine in Wine.objects.all():
		
	with open('csv/app_table.csv', 'r') as f:
		reader = csv.reader(f, delimiter=',')
		cnt=0
		matched=0
		for row in reader:
			cnt+=1

			prod_code = row[0]
			app = row[1]
			#print(prod_code, app)

			wine = Wine.objects.filter(product_code__iexact=prod_code)

			if wine.count() == 1:
				
				wine = wine[0]
				app, created = Appellation.objects.get_or_create(name=app)
				wine.appellation = app
				app.save()				
				wine.save()
				
				matched+=1
			else:
				print("%s" % prod_code)
				#pass
			
	print('Complete')
	print('Rows')
	print(cnt)
	print('Matched')
	print(matched)