from django.contrib import admin
from django.db import models
from .models import Wine, Producer, Varietal, PriceGroup, Size, Appellation, Employee, WholesaleWine, RetailWine

from .forms import WineForm, PriceGroupForm, VarietalForm, ProducerForm, AppellationForm
from import_export.admin import ImportExportActionModelAdmin
from adminsortable2.admin import SortableAdminMixin

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
	fields = ('producer', 'wine', 'colour', 'size', 'vintage', 'wholesale_price', 'case_size', 'wholesale_case_price' ,'product_code')
	readonly_fields = ( 'producer', 'vintage', 'size' , 'product_code', 'wholesale_case_price')
	extra = 0
	max_num=0

class EmployeeAdmin(SortableAdminMixin, admin.ModelAdmin):
	list_display = ('position','first_name', 'last_name' ,'email')
	list_editable = ('first_name', 'last_name' ,'email')
	
class AppellationAdmin(SortableAdminMixin, admin.ModelAdmin):
	form = AppellationForm
	list_display = ('name',)
	ordering = ('name',)
	inlines = (WineInline,)

class ProducerAdmin(SortableAdminMixin, admin.ModelAdmin):
	form = ProducerForm
	ordering = ('name',)
	search_fields = ('name',)
	inlines = (WineInline,)

class PriceGroupAdmin(SortableAdminMixin, admin.ModelAdmin):
	form = PriceGroupForm
	list_display = ('name',)
	inlines = (WineInline,)

class SizeAdmin(SortableAdminMixin, admin.ModelAdmin):
	list_display = ('name', 'size', 'id')
	list_editable = ('name',)

class VarietalAdmin(admin.ModelAdmin):
	form = VarietalForm
	list_display = ('name',)
	
class WineAdmin(ImportExportActionModelAdmin):

	resource_class = WineResource

	fieldsets = (
		(None, {
			'fields': ('short_name','wine' ,'producer', 'full_name', 'appellation', 'varietal', 'vintage', 'note', 'size', 'cost_price','retail_price', 'wholesale_price')
			}),
		('Availability', {
			"fields": ('retail', 'wholesale')
			}),
		('Linking Fields', {
			'classes': ('collapse',),
			'fields': ('sage_name','lcb_ref', 'octavian_ref')
			}),
		)
	save_as = True
	#list_filter = ['size', 'varietal', 'price_group' ,'vintage']
	
	#list_filter = ['wholesale', 'retail']

	search_fields = ['short_name' ,'vintage', 'product_code','producer__name']
	list_per_page = 50
	#list_display = ['vintage','short_name','wine' , 'producer','price_group' , 'size' , 'product_code', 'cost_price', 'retail', 'retail_price', 'wholesale', 'wholesale_price']
	list_display = ['vintage', 'wine', 'producer', 'short_name', 'size', 'product_code', 'cost_price','retail', 'retail_price', 'wholesale', 'wholesale_price']

	#list_editable = ['producer', 'size', 'wine', 'product_code','price_group', 'retail','wholesale', 'cost_price','retail_price', 'wholesale_price']
	list_editable = ['wine', 'size', 'product_code', 'retail', 'wholesale', 'cost_price', 'retail_price', 'wholesale_price']
	
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

class WholesaleWineAdmin(WineAdmin):
    #def get_queryset(self, request):
    #    return self.model.objects.filter(wholesale = True)
    list_display = ['product_code', 'wine', 'producer', 'vintage' , 'short_name', 'size', 'case_size', 'cost_price', 'wholesale_price' , 'wholesale_margin', 'bond_stock', 'cellar_stock', 'note']
    search_fields = ['product_code']
    list_filter = ['price_group']
    list_editable = []

class RetailWineAdmin(WineAdmin):
    #def get_queryset(self, request):
    #    return self.model.objects.filter(wholesale = True)
    list_display = ['short_name','product_code', 'size', 'case_size', 'vintage', 'cost_price', 'retail_price', 'cellar_stock', 'note']
    search_fields = ['product_code']
    list_editable = []
    list_filter = []

		
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Wine, WineAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Appellation, AppellationAdmin)
admin.site.register(PriceGroup, PriceGroupAdmin)
admin.site.register(Varietal, VarietalAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(WholesaleWine, WholesaleWineAdmin)
admin.site.register(RetailWine, RetailWineAdmin)
