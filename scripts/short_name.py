from inventory.models import Wine

def run():
	print('Started')
	for wine in Wine.objects.all():
		if wine.short_name is '':
			wine.short_name = wine.sage_name
			wine.save()
			print(wine.sage_name)

'''
psql -c "CREATE USER friarwood WITH PASSWORD 'friarwood'"

psql -c "GRANT ALL PRIVILEGES ON DATABASE friarwood TO friarwood"

6432

heroku config:add DATABASE_URL=postgres://friarwood:friarwood@52.16.41.189:6432/friarwood
'''