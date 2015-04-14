from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Wine, Producer, Varietal, Appellation
#from wines.tasks import find_wine

from import_export.admin import ImportExportActionModelAdmin

#Change admin site titles
admin.sites.AdminSite.site_header = 'Friarwood Fine Wines'
admin.sites.AdminSite.site_title = 'Friarwood'

#Resources

from import_export import resources

class WineResource(resources.ModelResource):
    class Meta:
        model = Wine

#Forms

from django import forms

class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = ['short_name', 'cost_price_s', 'retail_price_s', 'wholesale_price_s']
        widgets = {
        'short_name': TextInput(attrs={'size':'100'}),
        'cost_price_s': TextInput(attrs={'size':'5'}),
        'retail_price_s': TextInput(attrs={'size':'5'}),
        'wholesale_price_s': TextInput(attrs={'size':'5'}),
        'single_size': TextInput(attrs={'size':'5'}),
        }

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
			'fields': ('short_name', 'appellation', 'vintage', 'note')
			}),
		('Pricing', {
			'classes': ('grp-collapse','grp-closed'),
			'fields': ('cost_price_s','retail_price_s','wholesale_price_s')
			}),
		('Linking Fields', {
			'classes': ('grp-collapse','grp-closed'),
			'fields': ('sage_name','sage_ref','lcb_ref', 'octavian_ref')
			}),
		)
	list_display = ['short_name', 'sage_name', 'in_sage', 'stock_bin', 'single_size' , 'sage_ref', 'vintage', 'cost_price_s', 'retail_price_s', 'retail_margin', 'wholesale_price_s', 'wholesale_margin']
	list_filter = ['single_size','vintage']
	search_fields = ['short_name' ,'vintage', 'single_size']
	list_per_page = 500
	list_display_links = ['short_name']
	list_editable = ['single_size','cost_price_s', 'retail_price_s', 'wholesale_price_s']
	readonly_fields = ('sage_name','sage_ref',)

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
admin.site.register(Varietal)
admin.site.register(Appellation, AppellationAdmin)
