from django.http import HttpResponse
from .models import Wine, PriceGroup
from .pdf import createPDFPriceList
import csv

def pdf_creator(request):
	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="WineList.pdf"'
	
	# Create PDF from wine models
	createPDFPriceList(response)

	# Return PDF response
	return response

def eddy_export(request):
	# Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="shopifyexport.csv"'
    writer = csv.writer(response)
    writer.writerow([
	    	'Handle',
	    	'Title',
	    	'Body (HTML)',
	    	'Vendor',
	    	'Type',
	    	'Tags',
	    	'Published',
	    	'Option1 Name',
	    	'Option1 Value',
	    	'Option2 Name',
	    	'Option2 Value',
	    	'Option3 Name',
	    	'Option3 Value',
	    	'Variant SKU',
	    	'Variant Grams',
	    	'Variant Inventory Tracker',
	    	'Variant Inventory Qty',
	    	'Variant Inventory Policy',
	    	'Variant Fulfillment Service',
	    	'Variant Price',
	    	'Variant Compare At Price',
	    	'Variant Requires Shipping',
	    	'Variant Taxable',
	    	'Variant Barcode',
	    	'Image Src',
	    	'Image Alt Text',
	    	'Gift Card',
	    	'Google Shopping / MPN',
	    	'Google Shopping / Age Group',
	    	'Google Shopping / Gender',
	    	'Google Shopping / Google Product Category',
	    	'SEO Title',
	    	'SEO Description',
	    	'Google Shopping / AdWords Grouping',
	    	'Google Shopping / AdWords Labels',
	    	'Google Shopping / Condition',
	    	'Google Shopping / Custom Product',
	    	'Google Shopping / Custom Label 0',
	    	'Google Shopping / Custom Label 1',
	    	'Google Shopping / Custom Label 2',
	    	'Google Shopping / Custom Label 3',
	    	'Google Shopping / Custom Label 4',
	    	'Variant Image',
	    	'Variant Weight Unit'
	    ])
	

    for wine in Wine.objects.filter(wholesale=True):
	    writer.writerow([
	    	"%s-%s" % (
	    		wine.short_name.replace(' ','-').replace(',',''), 
	    		wine.vintage.replace(' ','-').replace(',','')
	    	) ,#'Handle',
	    	"%s, %s" % (wine.short_name, wine.vintage) ,#'Title',
	    	"%s, %s, %s" % (wine.wine,wine.producer ,wine.vintage), #'Body (HTML)',
	    	wine.producer,#'Vendor',
	    	'',#'Type',
	    	'', #'Tags',
	    	'', #'Published',
	    	'Size', #'Option1 Name',
	    	wine.size.size, #'Option1 Value',
	    	'',#'Option2 Name',
	    	'',	#'Option2 Value',
	    	'',#'Option3 Name',
	    	'',#'Option3 Value',
	    	wine.product_code,#'Variant SKU',
	    	'',#'Variant Grams',
	    	'',#'Variant Inventory Tracker',
	    	'0',#'Variant Inventory Qty',
	    	'deny',#'Variant Inventory Policy',
	    	'manual',#'Variant Fulfillment Service',
	    	wine.retail_price, #'Variant Price',
	    	'',#'Variant Compare At Price',
	    	'False' ,#'Variant Requires Shipping',
	    	'True' , #'Variant Taxable',
	    	'',#'Variant Barcode',
	    	'',#'Image Src',
	    	'',#'Image Alt Text',
	    	'',#'Gift Card',
	    	'',#'Google Shopping / MPN',
	    	'',#'Google Shopping / Age Group',
	    	'',#'Google Shopping / Gender',
	    	'',#'Google Shopping / Google Product Category',
	    	'',#'SEO Title',
	    	'',#'SEO Description',
	    	'',#'Google Shopping / AdWords Grouping',
	    	'',#'Google Shopping / AdWords Labels',
	    	'',#'Google Shopping / Condition',
	    	'',#'Google Shopping / Custom Product',
	    	'',#'Google Shopping / Custom Label 0',
	    	'',#'Google Shopping / Custom Label 1',
	    	'',#'Google Shopping / Custom Label 2',
	    	'',#'Google Shopping / Custom Label 3',
	    	'',#'Google Shopping / Custom Label 4',
	    	'',#'Variant Image',
	    	'',#'Variant Weight Unit'
	    ])

    return response

def shopify_export(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="shopifyexport.csv"'
    writer = csv.writer(response)
    writer.writerow([
	    	'Handle',
	    	'Title',
	    	'Body (HTML)',
	    	'Vendor',
	    	'Type',
	    	'Tags',
	    	'Published',
	    	'Option1 Name',
	    	'Option1 Value',
	    	'Option2 Name',
	    	'Option2 Value',
	    	'Option3 Name',
	    	'Option3 Value',
	    	'Variant SKU',
	    	'Variant Grams',
	    	'Variant Inventory Tracker',
	    	'Variant Inventory Qty',
	    	'Variant Inventory Policy',
	    	'Variant Fulfillment Service',
	    	'Variant Price',
	    	'Variant Compare At Price',
	    	'Variant Requires Shipping',
	    	'Variant Taxable',
	    	'Variant Barcode',
	    	'Image Src',
	    	'Image Alt Text',
	    	'Gift Card',
	    	'Google Shopping / MPN',
	    	'Google Shopping / Age Group',
	    	'Google Shopping / Gender',
	    	'Google Shopping / Google Product Category',
	    	'SEO Title',
	    	'SEO Description',
	    	'Google Shopping / AdWords Grouping',
	    	'Google Shopping / AdWords Labels',
	    	'Google Shopping / Condition',
	    	'Google Shopping / Custom Product',
	    	'Google Shopping / Custom Label 0',
	    	'Google Shopping / Custom Label 1',
	    	'Google Shopping / Custom Label 2',
	    	'Google Shopping / Custom Label 3',
	    	'Google Shopping / Custom Label 4',
	    	'Variant Image',
	    	'Variant Weight Unit'
	    ])
	

    for wine in Wine.objects.filter(wholesale=True):
	    writer.writerow([
	    	"%s-%s" % (
	    		wine.short_name.replace(' ','-').replace(',',''), 
	    		wine.vintage.replace(' ','-').replace(',','')
	    	) ,#'Handle',
	    	"%s, %s" % (wine.short_name, wine.vintage) ,#'Title',
	    	"%s, %s, %s" % (wine.wine,wine.producer ,wine.vintage), #'Body (HTML)',
	    	wine.producer,#'Vendor',
	    	'',#'Type',
	    	'', #'Tags',
	    	'', #'Published',
	    	'Size', #'Option1 Name',
	    	wine.size.size, #'Option1 Value',
	    	'',#'Option2 Name',
	    	'',	#'Option2 Value',
	    	'',#'Option3 Name',
	    	'',#'Option3 Value',
	    	wine.product_code,#'Variant SKU',
	    	'',#'Variant Grams',
	    	'',#'Variant Inventory Tracker',
	    	'0',#'Variant Inventory Qty',
	    	'deny',#'Variant Inventory Policy',
	    	'manual',#'Variant Fulfillment Service',
	    	wine.retail_price, #'Variant Price',
	    	'',#'Variant Compare At Price',
	    	'False' ,#'Variant Requires Shipping',
	    	'True' , #'Variant Taxable',
	    	'',#'Variant Barcode',
	    	'',#'Image Src',
	    	'',#'Image Alt Text',
	    	'',#'Gift Card',
	    	'',#'Google Shopping / MPN',
	    	'',#'Google Shopping / Age Group',
	    	'',#'Google Shopping / Gender',
	    	'',#'Google Shopping / Google Product Category',
	    	'',#'SEO Title',
	    	'',#'SEO Description',
	    	'',#'Google Shopping / AdWords Grouping',
	    	'',#'Google Shopping / AdWords Labels',
	    	'',#'Google Shopping / Condition',
	    	'',#'Google Shopping / Custom Product',
	    	'',#'Google Shopping / Custom Label 0',
	    	'',#'Google Shopping / Custom Label 1',
	    	'',#'Google Shopping / Custom Label 2',
	    	'',#'Google Shopping / Custom Label 3',
	    	'',#'Google Shopping / Custom Label 4',
	    	'',#'Variant Image',
	    	'',#'Variant Weight Unit'
	    ])

    return response


