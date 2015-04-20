from inventory.models import Wine, Producer, Size
import csv

def run():
	
	#for wine in Wine.objects.all():

	#0-short_name,1-case,2-bottle,3-vintage, 4-cost,5-wholesale,6-in_bond,7-cellar,8-prod_code, 9-notes
		
	with open('csv/master_product_table.csv', 'r') as f:
		reader = csv.reader(f, delimiter=',')
		cnt=0
		matched=0
		#print("Short Name, case, size, vintage, cost, wholesale, in_bond, cellar, prod_code, notes")
		for row in reader:

			prod_code = row[9] #done

			print(prod_code)

			wine = Wine.objects.filter(product_code__iexact=prod_code)

			if wine.count() == 1:
				wine = wine[0]
				wine.wholesale = True
				wine.save()
				
				matched+=1

			else:
				
				print("%s,%s" % (prod_code, 'Exception'))

			cnt+=1
			
	print('Complete')
	print('Rows')
	print(cnt)
	print('Matched')
	print(matched)


''' 
	0-Long Name 1-Short Name 2-Format 3-Vintage 4-Cost Price 5-wholesale-price 
	6-per case 7-in bond 8-Cellar 9-Product-Code 10-notes 
'''