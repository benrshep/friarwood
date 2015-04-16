from django.contrib import admin
from django.db import models
from .models import Wine, Producer, Varietal, PriceGroup, Size
from .forms import WineForm, PriceGroupForm, VarietalForm
from import_export.admin import ImportExportActionModelAdmin
from django.contrib.auth.decorators import user_passes_test
# WINE SEARCHER
#from wines.tasks import find_wine

from django.shortcuts import get_object_or_404

#Change admin site titles
admin.sites.AdminSite.site_header = 'Friarwood Fine Wines'
admin.sites.AdminSite.site_title = 'Friarwood'

def has_approval_permission(request, obj=None):
     if request.user.has_perm('blog.can_approve_post'):
         return True
     return False

# Resources

from import_export import resources

class WineResource(resources.ModelResource):
    class Meta:
        model = Wine

# Register your models here.

class WineInline(admin.TabularInline):
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

class VarietalAdmin(admin.ModelAdmin):
	form = VarietalForm
	list_display = ('name',)
	
class WineAdmin(ImportExportActionModelAdmin):
	resource_class = WineResource

	fieldsets = (
		(None, {
			'fields': ('short_name','producer', 'full_name', 'appellation', 'varietal', 'vintage', 'note', 'size', 'cost_price_s','retail_price_s', 'wholesale_price_s')
			}),
		('Linking Fields', {
			'classes': ('collapse',),
			'fields': ('sage_name','sage_ref','lcb_ref', 'octavian_ref')
			}),
		)
	
	list_filter = ['size', 'varietal', 'price_group' ,'vintage']
	search_fields = ['short_name' ,'vintage', 'sage_ref']
	list_per_page = 50
	list_display = ['short_name','vintage', 'producer','varietal', 'size' , 'product_code', 'sage_ref', 'cost_price_s', 'retail', 'retail_price_s', 'wholesale', 'wholesale_price_s']
	list_editable = ['varietal', 'product_code', 'retail','wholesale', 'cost_price_s','retail_price_s', 'wholesale_price_s']
	
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
admin.site.register(Varietal, VarietalAdmin)
