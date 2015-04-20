from django.db import models
import datetime

# Create your models here.		

class Wine(models.Model):
	"""docstring for  Wine"""

	wine = models.CharField(max_length=100, blank=True)
	
	short_name = models.CharField(max_length=100, blank=True)
	full_name = models.CharField(max_length=200, blank=True)

	producer = models.ForeignKey('Producer',null=True, blank=True)
	appellation = models.ForeignKey('Appellation',null=True, blank=True)
	varietal = models.ForeignKey('Varietal', null=True, blank=True)
	price_group = models.ForeignKey('PriceGroup',null=True, blank=True)

	vintage = models.CharField(max_length=50, blank=True)

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
	size = models.ForeignKey('Size', null=True, blank=True)

	note = models.TextField(blank = True, null=True)

	sku = models.CharField(max_length=200, blank=True)
	product_code = models.CharField(max_length=20, blank=True, null=True)
	l_win = models.CharField(max_length=200, blank=True)
	sage_name = models.CharField(max_length=100, blank=True)

	case_size = models.IntegerField(default=0)
	stocked = models.NullBooleanField()
	stock_bin = models.CharField(max_length=100)

	wholesale = models.BooleanField(default=False)
	pricelist = models.BooleanField(default=False)
	retail = models.BooleanField(default=False)
	#Added for stocklist
	bond_stock = models.CharField(max_length=6, blank=True, default=0)
	cellar_stock = models.CharField(max_length=6, blank=True, default=0)

	octavian_ref = models.CharField(max_length=100,blank=True, null = True)
	lcb_ref = models.CharField(max_length=100,blank=True, null = True)

	cost_price = models.DecimalField(max_digits=6, decimal_places=2,blank=True ,null=True)
	retail_price= models.DecimalField(max_digits=6, decimal_places=2,blank=True ,null=True)
	wholesale_price = models.DecimalField(max_digits=6, decimal_places=2,blank=True , null=True)
	
	my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

	class Meta(object):
		ordering = ('my_order',)

	def _in_sage(self):
		"Returns whether item in sage"
		if self.sage_name:
			return True
		else:
			return False

	def _retail_margin(self):
		"Returns the total"
		try:
			return str( round( (self.cost_price/self.retail_price)*100 ,2)) +'%'
		except: 
			return 'N/A'

	def _wholesale_margin(self):
		"Returns the total"
		try:
			return str( round( (self.cost_price/self.wholesale_price)*100 ,2)) +'%'
		except: 
			return 'N/A'

	def _wholesale_case(self):
		"Returns the total"
		try:
			return  round(self.wholesale_price*self.case_size, 2)
		except: 
			return '0'

	def _get_variants(self):
		try:
			return self.winevariant_set.all().count()
		except:
			return "None"

	variants = property(_get_variants)
	in_sage = property(_in_sage)
	retail_margin = property(_retail_margin)
	wholesale_margin = property(_wholesale_margin)
	wholesale_case_price = property(_wholesale_case)
	
	def __str__(self):
		return "%s : %s" % (self.short_name, self.vintage)

class WholesaleManager(models.Manager):
	def get_queryset(self):
		return super(WholesaleManager, self).get_queryset().filter(wholesale=True)

class WholesaleWine(Wine):
	objects = WholesaleManager()

	class Meta:
		proxy = True

class RetailManager(models.Manager):
	def get_queryset(self):
		return super(RetailManager, self).get_queryset().filter(retail=True)

class RetailWine(Wine):
    objects = RetailManager()
    class Meta:
        proxy = True

class Employee(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	position = models.CharField(max_length=200)
	email = models.CharField(max_length=200, blank=True)
	my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

	class Meta(object):
		ordering = ('my_order',)

	def __str__(self):
		return "%s %s" % (self.first_name, self.last_name)

class Producer(models.Model):
	"""docstring for  Producer"""
	name = models.CharField(max_length=200, unique=True)
	my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

	class Meta(object):
		ordering = ('my_order',)

	def __str__(self):
		return self.name

class PriceGroup(models.Model):
	"""docstring for  PriceGroup"""
	name = models.CharField(max_length=200, unique=True)
	details = models.TextField(blank = True, null = True)
	my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

	class Meta(object):
		ordering = ('my_order',)

	def __str__(self):
		return self.name

class Appellation(models.Model):
	"""docstring for  Varietal"""
	name = models.CharField(max_length=200, unique=True)
	country = models.CharField(max_length=200)
	my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

	class Meta(object):
		ordering = ('my_order',)

	def __str__(self):
		return self.name

class Varietal(models.Model):
	"""docstring for  Varietal"""
	name = models.CharField(max_length=200, unique=True)
	details = models.TextField(blank = True, null = True)
	my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

	class Meta(object):
		ordering = ('my_order',)

	def __str__(self):
		return self.name

class Size(models.Model):
	"""docstring for Size"""
	size = models.CharField(max_length=200, blank=True, unique=True)
	name = models.CharField(max_length=200, default='None')
	my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

	class Meta(object):
		ordering = ('my_order',)

	def __str__(self):
		return self.name

