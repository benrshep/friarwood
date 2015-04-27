from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Wine, Producer, Appellation, PriceGroup, Varietal

class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = ['short_name', 'producer','cost_price', 'retail_price', 'wholesale_price']
        widgets = { 
        'short_name': forms.TextInput(attrs={'size':'100'}),
        'vintage': forms.TextInput(attrs={'size':'5'}),
        'wine': forms.TextInput(attrs={'size':'25'}),
        'cost_price': forms.TextInput(attrs={'size':'5'}),
        'retail_price': forms.TextInput(attrs={'size':'5'}),
        'wholesale_price': forms.TextInput(attrs={'size':'5'}),
        'single_size': forms.TextInput(attrs={'size':'5'}),
        'product_code': forms.TextInput(attrs={'size':'9'}),
        'producer': forms.Select(attrs={'style':'width:180px'}),
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

class ProducerForm(forms.ModelForm):
	class Meta:
		model = Producer
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
		super(ProducerForm, self).__init__(*args, **kwargs)
		if self.instance.pk:
			self.fields['wines'].initial = self.instance.wine_set.all()
	def save(self, commit=True):
		producer = super(ProducerForm, self).save(commit=False)  

		if commit:
			producer.save()

		if producer.pk:
			producer.wine_set = self.cleaned_data['wines']
			self.save_m2m()
		return producer

class AppellationForm(forms.ModelForm):
	class Meta:
		model = Appellation
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
		super(AppellationForm, self).__init__(*args, **kwargs)
		if self.instance.pk:
			self.fields['wines'].initial = self.instance.wine_set.all()
	def save(self, commit=True):
		appellation = super(AppellationForm, self).save(commit=False)  

		if commit:
			appellation.save()

		if appellation.pk:
			appellation.wine_set = self.cleaned_data['wines']
			self.save_m2m()
		return appellation
