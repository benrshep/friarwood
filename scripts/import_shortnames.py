from inventory.models import Wine, Producer, Size
import csv

def run():
	
	#for wine in Wine.objects.all():
		
	with open('csv/master_product_table.csv', 'r') as f:
		reader = csv.reader(f, delimiter=',')
		cnt=0
		matched=0
		for row in reader:

			#case = row[2].split('x')[0] #done
			#size = row[2].split('x')[1] #done
			short_name = row[1] #done
			#vintage = row[3] #done
			#cost = row[4] #done
			#wholesale = row[5] #done
			#in_bond = row[7] #done
			#cellar = row[8] #done
			prod_code = row[9] #done
			#notes = row[10] #done

			wine = Wine.objects.filter(product_code__iexact=prod_code)

			if wine.count() == 1:
				
				wine = wine[0]

				wine.short_name = short_name
				#wine.cost_price_s = cost
				#wine.wholesale_price_s = wholesale
				#wine.product_code = prod_code
				#wine.case_size = case
				#wine.note = notes
				#wine.bond_stock = in_bond
				#wine.cellar_stock = cellar
				
				wine.save()
				
				matched+=1
				
				#print("%s,%s" % (short_name, vintage))
				#print('|')
				#print(wine)
			else:
				print("%s" % (prod_code,))
			
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