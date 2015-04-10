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
				new_wine = Wine(short_name=row[15], vintage=row[16], single_size=row[17],cost_price=row[18],retail_price=[20])
				new_wine.save()
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
								handled+=1
						else:
							#ADD WINE
							new_wine = Wine(short_name=row[15], vintage=row[16], single_size=row[17],cost_price=row[18],retail_price=[20])
							new_wine.save()
							handled+=1

					elif row[17] == '1.5' or row[17] == '1.50':
						if 'mag' in sage:
							if vint == row[16]:
								#UPDATE WINE
								handled+=1
						else:
							#ADD WINE
							new_wine = Wine(short_name=row[15], vintage=row[16], single_size=row[17],cost_price=row[18],retail_price=[20])
							new_wine.save()
							handled+=1

					elif row[17] == '0.5' or row[17] == '0.7':
						#ADD WINE
						new_wine = Wine(short_name=row[15], vintage=row[16], single_size=row[17],cost_price=row[18],retail_price=[20])
						new_wine.save()
						#print("%s, %s, %s" % (row[17],row[15],row[16]))
						#print("%s" % wine)
						handled+=1

					else:
						if vint == row[16]:
							#UPDATE WINE
							handled+=1

		total = n_found+found
		h_total = handled+n_handled
		print("Found: %d" % found)
		print("Handled: %d" % handled)
		print("Not Found: %d" % n_found)
		print("Not Found Handled: %d" % n_handled)
		print("Total: %d" % total)
		print("Rows: %d" % rows)
		
		
		print("Handled Total: %d" % h_total)


			#w = Wine(sage_ref=row[0], sage_name=row[1],)
			#w.save()