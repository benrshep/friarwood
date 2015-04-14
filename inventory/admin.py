from django.contrib import admin
from .models import Wine, Producer, Varietal, Appellation
#from wines.tasks import find_wine

from import_export import resources
from import_export.admin import ImportExportActionModelAdmin


class WineResource(resources.ModelResource):

    class Meta:
        model = Wine

# Register your models here.

class WineInline(admin.StackedInline):
	model = Wine
	fields = ['wine', 'vintage']
	extra = 1

class ProducerAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['producer']}),]
	inlines = [WineInline]

class AppellationAdmin(admin.ModelAdmin):
	list_display = ['name','country']

class WineAdmin(ImportExportActionModelAdmin):
	resource_class = WineResource
	fieldsets = (
		(None, {
			'fields': ('sage_name', 'appellation', 'vintage', 'note')
			}),
		('Pricing', {
			'classes': ('grp-collapse','grp-closed'),
			'fields': ('cost_price_s','retail_price_s','wholesale_price_s')
			}),
		('Linking Fields', {
			'classes': ('grp-collapse','grp-closed'),
			'fields': ('sage_ref','lcb_ref', 'octavian_ref')
			}),
		)
	list_display = ['short_name', 'sage_name', 'stock_bin', 'single_size' , 'sage_ref', 'vintage', 'cost_price_s', 'retail_price_s', 'wholesale_price_s']
	list_filter = ['vintage', 'retail_price_s']
	search_fields = ['sage_name','short_name' ,'vintage', 'single_size']
	list_per_page = 500

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
admin.site.register(Varietal)
admin.site.register(Appellation, AppellationAdmin)
