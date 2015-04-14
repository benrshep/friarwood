import csv
from inventory.models import Wine

def run():
	with open('retail.csv', 'r') as f:
		reader = csv.reader(f, delimiter=',')
		n_found = 0
		found = 0
		total=0
		n_handled=0
		handled=0
		rows=0
		for row in reader:
			rows+=1
			w = Wine.objects.filter(sage_name__contains=row[15])
			#print(w)
			if w.count() < 1:
				n_found+=1
				#ADD WINE
				nwine = Wine(stock_bin = row[0],short_name=row[15], vintage=row[16], single_size=row[17],cost_price_s=row[18],retail_price_s=row[20])
				nwine.save()
				n_handled+=1

			else:
				found+=1
				for wine in w:
					sage = wine.sage_name.lower()
					vint = wine.vintage
					if row[17] == '0.375':
						if 'half' in sage:
							if vint == row[16]:
								#UPDATE WINE
								wine.short_name = row[15]
								wine.vintage = row[16]
								wine.single_size = row[17]
								wine.cost_price_s = row[18]
								wine.retail_price_s = row[20]
								wine.stock_bin = row[0]
								wine.save()
								handled+=1
						else:
							#ADD WINE
							nwine = Wine(stock_bin = row[0],short_name=row[15], vintage=row[16], single_size=row[17],cost_price_s=row[18],retail_price_s=row[20])
							nwine.save()
							handled+=1

					elif row[17] == '1.5' or row[17] == '1.50':
						if 'mag' in sage:
							if vint == row[16]:
								#UPDATE WINE
								wine.short_name = row[15]
								wine.vintage = row[16]
								wine.single_size = row[17]
								wine.cost_price_s = row[18]
								wine.retail_price_s = row[20] 
								wine.stock_bin = row[0]
								wine.save()
								handled+=1
						else:
							#ADD WINE
							nwine = Wine(stock_bin = row[0],short_name=row[15], vintage=row[16], single_size=row[17],cost_price_s=row[18],retail_price_s=row[20])
							nwine.save()
							handled+=1

					elif row[17] == '0.5' or row[17] == '0.7':
						#ADD WINE
						nwine = Wine(stock_bin = row[0],short_name=row[15], vintage=row[16], single_size=row[17],cost_price_s=row[18],retail_price_s=row[20])
						nwine.save()
						handled+=1

					elif row[17] == '0.75':
						if vint == row[16] and 'half' not in sage:
							#UPDATE WINE
							wine.short_name = row[15]
							wine.vintage = row[16]
							wine.single_size = row[17]
							wine.cost_price_s = row[18]
							wine.retail_price_s = row[20]
							wine.stock_bin = row[0]
							wine.save()
							handled+=1

		#print("%s, %s, %s" % (row[17],row[15],row[16]))
		#print("%s" % wine)

		total = n_found+found
		h_total = handled+n_handled
		print("Found: %d" % found)
		print("Handled: %d" % handled)
		print("Not Found: %d" % n_found)
		print("Not Found Handled: %d" % n_handled)
		print("Total: %d" % total)
		print("Rows: %d" % rows)
		
		print("Handled Total: %d" % h_total)

