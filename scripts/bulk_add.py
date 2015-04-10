import csv
from inventory.models import Wine

def run():
	with open('prodtable.csv', 'r') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			w = Wine(sage_ref=row[0], sage_name=row[1],)
			w.save()

			'''
			with open('prodtable.csv', 'rb') as csvfile:
				prodreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

				print(prodreader(1))

				for row in prodreader:
					print('test')
					w = Wine(sage_ref=row[0], sage_name=row[1],)
					w.save()
					'''