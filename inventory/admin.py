from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Wine, Producer, Appellation, PriceGroup, WineVariant
#from wines.tasks import find_wine

from import_export.admin import ImportExportActionModelAdmin

from django.contrib.admin.widgets import FilteredSelectMultiple

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

class VariantForm(forms.ModelForm):
    class Meta:
        model = WineVariant
        
        fields = ['single_size', 'sage_name', 'cost_price_s','retail_price_s', 'wholesale_price_s']
        widgets = {
        'single_size': TextInput(attrs={'size':'100'}),
        'cost_price_s': TextInput(attrs={'size':'15'}),
        'retail_price_s': TextInput(attrs={'size':'15'}),
        'wholesale_price_s': TextInput(attrs={'size':'15'}),
        'single_size': TextInput(attrs={'size':'15'}),
        }

class PriceGroupForm(forms.ModelForm):
	class Meta:
		model = PriceGroup
		fields = ('name',)

	wines = forms.ModelMultipleChoiceField(
		queryset=Wine.objects.all(),
		required=False,
		widget=FilteredSelectMultiple(
			verbose_name='Wines',
			is_stacked=False
			)
		)
	def __init__(self, *args, **kwargs):
		super(PriceGroupForm, self).__init__(*args, **kwargs)
		if self.instance.pk:
			self.fields['wines'].initial = self.instance.wine_set.all()
	def save(self, commit=True):
		price_group = super(PriceGroupForm, self).save(commit=False)  

		if commit:
			price_group.save()

		if price_group.pk:
			price_group.wine_set = self.cleaned_data['wines']
			self.save_m2m()
		return price_group

# Register your models here.

class WineInline(admin.StackedInline):
	model = Wine
	fields = ['wine', 'vintage']
	extra = 1

class WineVariantInline(admin.TabularInline):
	model = WineVariant
	form = VariantForm
	readonly_fields = ('in_sage', 'wholesale_margin', 'retail_margin')
	fields = ['single_size','in_sage', 'sage_name', 'cost_price_s','retail_price_s', 'retail_margin', 'wholesale_price_s','wholesale_margin']
	extra = 0

class ProducerAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['producer']}),]
	inlines = [WineInline]

class AppellationAdmin(admin.ModelAdmin):
	list_display = ['name','country']

class PriceGroupAdmin(admin.ModelAdmin):
	form = PriceGroupForm
	list_display = ('name',)
	
class WineAdmin(ImportExportActionModelAdmin):
	resource_class = WineResource
	fieldsets = (
		(None, {
			'fields': ('short_name', 'full_name', 'appellation', 'vintage', 'note')
			}),
		('Linking Fields', {
			'classes': ('collapse',),
			'fields': ('sage_name','sage_ref','lcb_ref', 'octavian_ref')
			}),
		)
	
	inlines = [WineVariantInline]
	list_display = ['short_name', 'variants', 'single_size' , 'product_code', 'sage_ref', 'vintage']
	list_filter = ['single_size','vintage']
	search_fields = ['short_name' ,'vintage', 'single_size']
	list_per_page = 500
	list_display_links = ['short_name']
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
admin.site.register(PriceGroup, PriceGroupAdmin)
admin.site.register(Appellation, AppellationAdmin)
