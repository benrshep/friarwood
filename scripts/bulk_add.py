import csv
from inventory.models import Wine

def run():
	with open('prodtable.csv', 'r') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			w = Wine(sage_ref=row[0], sage_name=row[1],)
			w.save()

	print('Complete')