from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Wine, Producer, Appellation, PriceGroup, Varietal

class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = ['short_name', 'producer','cost_price_s', 'retail_price_s', 'wholesale_price_s']
        widgets = { 
        'short_name': forms.TextInput(attrs={'size':'100'}),
        'cost_price_s': forms.TextInput(attrs={'size':'5'}),
        'retail_price_s': forms.TextInput(attrs={'size':'5'}),
        'wholesale_price_s': forms.TextInput(attrs={'size':'5'}),
        'single_size': forms.TextInput(attrs={'size':'5'}),
        'product_code': forms.TextInput(attrs={'size':'10'}),
        'producer': forms.Select(attrs={'style':'width:150px'}),
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

class VarietalForm(forms.ModelForm):
	class Meta:
		model = Varietal
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
		super(VarietalForm, self).__init__(*args, **kwargs)
		if self.instance.pk:
			self.fields['wines'].initial = self.instance.wine_set.all()
	def save(self, commit=True):
		varietal = super(VarietalForm, self).save(commit=False)  

		if commit:
			varietal.save()

		if varietal.pk:
			varietal.wine_set = self.cleaned_data['wines']
			self.save_m2m()
		return varietal
