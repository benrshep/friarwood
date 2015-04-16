import csv
from inventory.models import Wine

def run():
	with open('whole.csv', 'r') as f:
		reader = csv.reader(f, delimiter=',')
		n_found = 0
		found = 0
		total=0
		n_handled=0
		handled=0
		rows=0
		for row in reader:
			rows+=1
			w = Wine.objects.filter(short_name__contains=row[0])
			#print(w)
			if w.count() < 1:
				n_found+=1
				#ADD WINE
				nwine = Wine(short_name=row[0], vintage=row[1], single_size=row[3],w_cost_price_s=row[4],wholesale_price_s=row[5],note=row[7])
				nwine.save()
				n_handled+=1

			else:
				found+=1
				for wine in w:
					size = wine.single_size
					vint = wine.vintage
					if row[3] == '0.375' and size == '0.375':
						if vint == row[1]:
							#UPDATE WINE
							wine.short_name = row[0]
							wine.vintage = row[1]
							wine.single_size = row[3]
							wine.w_cost_price_s = row[4]
							wine.wholesale_price_s = row[5]
							wine.note = row[7]
							wine.save()
							handled+=1
						
					elif row[3] == '1.5' or row[3] == '1.50' and size == '1.5':
						if vint == row[1]:
							#UPDATE WINE
							wine.short_name = row[0]
							wine.vintage = row[1]
							wine.single_size = row[3]
							wine.w_cost_price_s = row[4]
							wine.wholesale_price_s = row[5] 
							wine.note = row[7]
							wine.save()
							handled+=1
						
					elif row[3] == '0.75':
						if vint == row[1] and '0.375' not in size:
							#UPDATE WINE
							wine.short_name = row[0]
							wine.vintage = row[1]
							wine.single_size = row[3]
							wine.w_cost_price_s = row[4]
							wine.wholesale_price_s = row[5]
							wine.note = row[7]
							wine.save()
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

