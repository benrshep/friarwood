from django.contrib import admin
from django.db import models
from .models import Wine, Producer, Varietal, PriceGroup, Size, Appellation
from .forms import WineForm, PriceGroupForm, VarietalForm, ProducerForm, AppellationForm
from import_export.admin import ImportExportActionModelAdmin
# WINE SEARCHER
#from wines.tasks import find_wine

from django.shortcuts import get_object_or_404

#Change admin site titles
admin.sites.AdminSite.site_header = 'Friarwood Fine Wines'
admin.sites.AdminSite.site_title = 'Friarwood'

# Resources

from import_export import resources

class WineResource(resources.ModelResource):
    class Meta:
        model = Wine

# Register your models here.

class WineInline(admin.TabularInline):
	model = Wine
	verbose_name= False
	show_change_link = True
	ordering = ("producer",)
	fields = ('producer', 'wine', 'size' , 'vintage', 'wholesale_price_s', 'case_size', 'wholesale_case_price' ,'product_code')
	readonly_fields = ( 'producer', 'vintage', 'size' , 'product_code', 'wholesale_case_price')
	extra = 0
	max_num=0
	
class AppellationAdmin(admin.ModelAdmin):
	form = AppellationForm
	list_display = ('name',)
	inlines = (WineInline,)

class ProducerAdmin(admin.ModelAdmin):
	form = ProducerForm
	ordering = ('name',)
	search_fields = ('name',)
	

class PriceGroupAdmin(admin.ModelAdmin):
	form = PriceGroupForm
	list_display = ('name',)
	inlines = (WineInline,)


class SizeAdmin(admin.ModelAdmin):
	list_display = ('name', 'size')
	list_editable = ('name',)

class VarietalAdmin(admin.ModelAdmin):
	form = VarietalForm
	list_display = ('name',)
	
class WineAdmin(ImportExportActionModelAdmin):
	resource_class = WineResource

	fieldsets = (
		(None, {
			'fields': ('short_name','wine' ,'producer', 'full_name', 'appellation', 'varietal', 'vintage', 'note', 'size', 'cost_price_s','retail_price_s', 'wholesale_price_s')
			}),
		('Linking Fields', {
			'classes': ('collapse',),
			'fields': ('sage_name','sage_ref','lcb_ref', 'octavian_ref')
			}),
		)
	save_as = True
	#list_filter = ['size', 'varietal', 'price_group' ,'vintage']
	search_fields = ['short_name' ,'vintage', 'producer__name', 'sage_ref']
	list_per_page = 50
	list_display = ['short_name','vintage','wine' , 'producer', 'size' , 'product_code', 'sage_ref', 'cost_price_s', 'retail', 'retail_price_s', 'wholesale', 'wholesale_price_s']
	list_editable = ['producer','sage_ref' , 'vintage', 'size', 'wine', 'product_code', 'retail','wholesale', 'cost_price_s','retail_price_s', 'wholesale_price_s']
	#list_editable = ['product_code','retail','wholesale']
	
	def get_changelist_form(self, request, **kwargs):
		return WineForm

	def save_model(self, request, obj, form, change):
		#Save initial required infomation
		obj.sage_name = obj.sage_name.title()
		#obj.wine = obj.wine.title()
		#obj.searcher_status = "Processing"
		#obj.searcher_url = "http://www.wine-searcher.com/find/%s/%s" % (obj.wine.replace(',','').replace(' ','+').lower(), obj.vintage)
		#Start wine searcher scraper
		#find_wine.delay(obj)
		obj.save()
		
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Wine, WineAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Appellation, AppellationAdmin)
admin.site.register(PriceGroup, PriceGroupAdmin)
admin.site.register(Varietal, VarietalAdmin)
