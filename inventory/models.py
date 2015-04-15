from django.db import models
import datetime

# Create your models here.

class Producer(models.Model):
	"""docstring for  Producer"""
	name = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.name

class PriceGroup(models.Model):
	"""docstring for  Varietal"""
	name = models.CharField(max_length=200, unique=True)
	details = models.TextField(blank = True, null = True)

	def __str__(self):
		return self.name

class Varietal(models.Model):
	"""docstring for  Varietal"""
	name = models.CharField(max_length=200, unique=True)
	details = models.TextField(blank = True, null = True)

	def __str__(self):
		return self.name

class Appellation(models.Model):
	"""docstring for  Varietal"""
	name = models.CharField(max_length=200, unique=True)
	country = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.name

class Wine(models.Model):
	"""docstring for  Wine"""
	wine = models.CharField(max_length=100)
	
	short_name = models.CharField(max_length=100, blank=True)
	full_name = models.CharField(max_length=200, blank=True)

	producer = models.ForeignKey('Producer',null=True, blank=True)
	appellation = models.ForeignKey('Appellation',null=True, blank=True)

	vintage = models.CharField(max_length=50, blank=True)
	price_group = models.ForeignKey('PriceGroup',null=True, blank=True)

	searcher_details = models.NullBooleanField(default=False)
	searcher_url = models.CharField(max_length=200, blank=True)
	searcher_price = models.DecimalField(max_digits=6, decimal_places=2, default = 0)
	searcher_status = models.CharField(max_length=100, blank=True, null = True)
	searcher_data = models.TextField(blank= True, null=True)

	colour = models.CharField(max_length=100)
	wine_type = models.CharField(max_length=100)
	alcohol = models.DecimalField(max_digits=3, decimal_places=2,default=0)
	classification = models.CharField(max_length=200)

	#Variations

	single_size = models.CharField(max_length=50, blank=True)

	note = models.TextField(blank = True, null=True)

	sku = models.CharField(max_length=200, blank=True)
	product_code = models.CharField(max_length=20, blank=True, null=True)
	l_win = models.CharField(max_length=200, blank=True)
	sage_name = models.CharField(max_length=100, blank=True)

	case_size = models.IntegerField(default=0)
	stocked = models.NullBooleanField()
	stock_bin = models.CharField(max_length=100)

	wholesale = models.BooleanField(default=True)
	pricelist = models.BooleanField(default=True)
	retail = models.BooleanField(default=True)
	

	octavian_ref = models.CharField(max_length=100,blank=True, null = True)
	lcb_ref = models.CharField(max_length=100,blank=True, null = True)
	sage_ref = models.CharField(max_length=100,blank=True, null = True)

	cost_price_s = models.CharField(max_length=100,blank=True, null = True)
	w_cost_price_s = models.CharField(max_length=100,blank=True, null = True)
	cost_price = models.DecimalField(max_digits=6, decimal_places=2,blank=True, null = True)

	retail_price_s = models.CharField(max_length=100,blank=True, null = True)
	retail_price= models.DecimalField(max_digits=6, decimal_places=2,blank=True, null = True)

	wholesale_price_s = models.CharField(max_length=100,blank=True, null = True)
	wholesale_price = models.DecimalField(max_digits=6, decimal_places=2,blank=True, null = True)

	def _get_variants(self):
		try:
			return self.winevariant_set.all().count()
		except:
			return "None"

	variants = property(_get_variants)

	def __str__(self):
		return self.sage_name

class WineVariant(models.Model):

	wine = models.ForeignKey('Wine')
	single_size = models.CharField(max_length=50, blank=True)

	sku = models.CharField(max_length=200, blank=True, null=True)
	product_code = models.CharField(max_length=20, blank=True, null=True)
	l_win = models.CharField(max_length=200, blank=True)
	sage_name = models.CharField(max_length=100, blank=True, null=True)
	note = models.TextField(blank = True, null=True)


	case_size = models.IntegerField(default=0)
	stocked = models.NullBooleanField()
	stock_bin = models.CharField(max_length=100, null = True)

	wholesale = models.BooleanField(default=True)
	pricelist = models.BooleanField(default=True)
	retail = models.BooleanField(default=True)

	octavian_ref = models.CharField(max_length=100,blank=True, null = True)
	lcb_ref = models.CharField(max_length=100,blank=True, null = True)
	sage_ref = models.CharField(max_length=100,blank=True, null = True)

	
	w_cost_price_s = models.CharField(max_length=100,blank=True, null = True)
	cost_price_s = models.CharField(max_length=100,blank=True, null = True)
	cost_price = models.DecimalField(max_digits=6, decimal_places=2,blank=True, null = True)

	retail_price_s = models.CharField(max_length=100,blank=True, null = True)
	retail_price= models.DecimalField(max_digits=6, decimal_places=2,blank=True, null = True)

	wholesale_price_s = models.CharField(max_length=100,blank=True, null = True)
	wholesale_price = models.DecimalField(max_digits=6, decimal_places=2,blank=True, null = True)

	def _in_sage(self):
		"Returns whether item in sage"
		if self.sage_name:
			return True
		else:
			return False

	def _retail_margin(self):
		"Returns the total"
		try:
			return  str(round((float(self.cost_price_s) / float(self.retail_price_s))*100, 2)) + '%' 
		except: 
			return 'N/A'

	def _wholesale_margin(self):
		"Returns the total"
		try:
			return  str(round((float(self.cost_price_s) / float(self.wholesale_price_s))*100, 2)) + '%' 
		except: 
			return 'N/A'

	in_sage = property(_in_sage)
	retail_margin = property(_retail_margin)
	wholesale_margin = property(_wholesale_margin)

	def __str__(self):
		return ('%s : %s' % (self.wine.short_name,self.single_size))


