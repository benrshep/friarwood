from inventory.models import Wine, Producer, Size
import csv

def run():
	
	#for wine in Wine.objects.all():

	#0-short_name,1-case,2-bottle,3-vintage, 4-cost,5-wholesale,6-in_bond,7-cellar,8-prod_code, 9-notes
		
	with open('missing.csv', 'r') as f:
		reader = csv.reader(f, delimiter=',')
		cnt=0
		matched=0
		#print("Short Name, case, size, vintage, cost, wholesale, in_bond, cellar, prod_code, notes")
		for row in reader:

			case = row[1]
			size = row[2] #done
			short_name = row[0] #done
			vintage = row[3] #done
			cost = row[4] #done
			wholesale = row[5] #done
			in_bond = row[6] #done
			cellar = row[7] #done
			prod_code = row[8] #done
			notes = row[9] #done

			print(prod_code)

			wine = Wine.objects.filter( product_code__iexact=prod_code )

			if wine.count() == 1:
				wine = wine[0]
				
				wine.cost_price_s = cost
				wine.wholesale_price_s = wholesale
				wine.case_size = case
				wine.note = notes
				wine.bond_stock = in_bond
				wine.cellar_stock = cellar
				wine.save()
				
				matched+=1
				
				#print("%s,%s" % (short_name, vintage))
				#print('|')
				#print(wine)
			else:
				print("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (short_name, case, size, vintage, cost, wholesale, in_bond, cellar, prod_code, notes))
			
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