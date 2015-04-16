from django.contrib import admin
from django.db import models
from .models import Wine, Producer, Varietal, PriceGroup, Size

from import_export.admin import ImportExportActionModelAdmin
from .forms import WineForm, PriceGroupForm

# WINE SEARCHER
#from wines.tasks import find_wine

#Change admin site titles
admin.sites.AdminSite.site_header = 'Friarwood Fine Wines'
admin.sites.AdminSite.site_title = 'Friarwood'

# Resources

from import_export import resources

class WineResource(resources.ModelResource):
    class Meta:
        model = Wine

# Register your models here.

class WineInline(admin.StackedInline):
	model = Wine
	fields = ['short_name', 'vintage']
	extra = 0

class ProducerAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['name']}),]
	ordering = ('name',)
	inlines = [WineInline]

class PriceGroupAdmin(admin.ModelAdmin):
	form = PriceGroupForm
	list_display = ('name',)

class SizeAdmin(admin.ModelAdmin):
	list_display = ('name', 'size')
	list_editable = ('name',)

	
class WineAdmin(ImportExportActionModelAdmin):
	resource_class = WineResource
	fieldsets = (
		(None, {
			'fields': ('producer', 'full_name', 'appellation', 'vintage', 'note')
			}),
		('Linking Fields', {
			'classes': ('collapse',),
			'fields': ('sage_name','sage_ref','lcb_ref', 'octavian_ref')
			}),
		)
		
	list_display = ['short_name','vintage', 'producer','varietal', 'size' , 'product_code', 'sage_ref', 'cost_price_s','retail_price_s', 'wholesale_price_s']
	list_filter = ['size', 'varietal', 'price_group' ,'vintage']
	search_fields = ['short_name' ,'vintage']
	list_per_page = 50
	#readonly_fields = ('sage_name','sage_ref',)
	list_editable = ['producer','varietal', 'size', 'cost_price_s','retail_price_s', 'wholesale_price_s']

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
admin.site.register(PriceGroup, PriceGroupAdmin)
admin.site.register(Varietal)
