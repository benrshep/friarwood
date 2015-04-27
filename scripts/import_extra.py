from inventory.models import Wine, Producer, Size, Appellation, Region
import csv

def run():
	
	#for wine in Wine.objects.all():
		
	with open('csv/prod_table.csv', 'r') as f:
		reader = csv.reader(f, delimiter=',')
		cnt=0
		matched=0
		print("Short Name, case, size, vintage, cost, wholesale, in_bond, cellar, prod_code, notes")
		for row in reader:

			list_name = row[0].title() #Wine List name
			clean_name = row[1] #Clean name
			region = row[2].title() #Region
			appellation = row[3].title() #Appelation
			#format = row[4] #Format
			#case = row[4].split('x')[0] #done
			#size = row[4].split('x')[1] #done
			vintage = row[5] #Vintage
			cost = row[6] # Cost price
			wholesale = row[7] #List price per bottle
			#List price per case= row[8] #List price per case
			bond = row[9]
			cellar = row[10]
			product_code = row[11]
			notes = row[12]
			#Margin = row[13]

			wine = Wine.objects.filter(product_code__iexact=product_code)

			if wine.count() == 1:
				
				wine = wine[0]

				if wine.vintage != vintage:
					print(wine.product_code)
					print(product_code)
					print("Vintage Error: ", wine)
				'''
				try:
					cp = ''.join(_ for _ in cost if _ in ".1234567890")
					wine.cost_price = float(cp)
				except:
					wine.note = wine.note + 'Import Error: No Cost Price'
				try:
					wp = ''.join(_ for _ in wholesale if _ in ".1234567890")
					wine.wholesale_price = float(wp)
				except:
					wine.note = wine.note + 'Import Error: No Wholesale Price'

				app, created = Appellation.objects.get_or_create(name=appellation)
				app.save()
				wine.appellation = app
				
				reg, reated = Region.objects.get_or_create(name=region)
				reg.save()
				wine.region = reg
				'''
				#wine.product_code = prod_code
				#wine.case_size = case
				#wine.note = wine.note + notes
				wine.wine = list_name.title()
				wine.bond_stock = bond
				wine.cellar_stock = cellar
				wine.save()
				
				matched+=1
				
				#print("%s,%s" % (short_name, vintage))
				#print('|')
				#print(wine)
			else:
				print("\n", product_code)
				print("err", wine)
				print("Error updating: %s,%s,%s" % (list_name, clean_name, vintage))
			
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