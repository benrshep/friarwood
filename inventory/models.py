from django.db import models
import datetime

# Create your models here.

class Producer(models.Model):
	"""docstring for  Producer"""
	name = models.CharField(max_length=200, unique=True)

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
	sage_name = models.CharField(max_length=100)
	short_name = models.CharField(max_length=100, blank=True)
	full_name = models.CharField(max_length=200, blank=True)
	sku = models.CharField(max_length=200, blank=True)
	l_win = models.CharField(max_length=200, blank=True)
	
	varietal = models.ForeignKey('Varietal',null=True, blank=True)
	producer = models.ForeignKey('Producer',null=True, blank=True)
	appellation = models.ForeignKey('Appellation',null=True, blank=True)

	vintage = models.CharField(max_length=50, blank=True)

	searcher_details = models.NullBooleanField(default=False)
	searcher_url = models.CharField(max_length=200, blank=True)
	searcher_price = models.DecimalField(max_digits=6, decimal_places=2, default = 0)
	searcher_status = models.CharField(max_length=100, blank=True, null = True)
	searcher_data = models.TextField(blank= True, null=True)

	
	region1 = models.CharField(max_length=100)
	region2 = models.CharField(max_length=100)
	region3 = models.CharField(max_length=100)
	region4 = models.CharField(max_length=100)
	region5 = models.CharField(max_length=100)
	
	colour = models.CharField(max_length=100)
	wine_type = models.CharField(max_length=100)
	alcohol = models.DecimalField(max_digits=3, decimal_places=2,default=0)
	classification = models.CharField(max_length=200)
	
	single_size = models.IntegerField(default=0)
	case_size = models.IntegerField(default=0)
	case_type = models.CharField(max_length=100)
	stocked = models.NullBooleanField()
	stock_bin = models.CharField(max_length=100)

	wholesale = models.BooleanField(default=True)
	retail = models.BooleanField(default=True)
	note = models.TextField(blank = True, null=True)

	octavian_ref = models.CharField(max_length=100,blank=True, null = True)
	lcb_ref = models.CharField(max_length=100,blank=True, null = True)
	sage_ref = models.CharField(max_length=100,blank=True, null = True)

	cost_price = models.DecimalField(max_digits=6, decimal_places=2,null=True, blank=True)
	retail_price = models.DecimalField(max_digits=6, decimal_places=2,null=True, blank=True)
	retail_price_vat = models.DecimalField(max_digits=6, decimal_places=2,null=True,blank=True)
	wholesale_price = models.DecimalField(max_digits=6, decimal_places=2,null=True, blank=True)
	wholesale_price_vat = models.DecimalField(max_digits=6, decimal_places=2,null=True, blank=True)
	retail_margin = models.IntegerField(default=0)
	wholesale_margin = models.IntegerField(default=0)
	vat = models.IntegerField(default=20)

	def __str__(self):
		return self.sage_name

