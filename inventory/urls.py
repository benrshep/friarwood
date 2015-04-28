from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='data'),
	#ONLINE LIST
	url(r'^retail/', views.retailView, name='retail_view'),
	#PDF LIST
	url(r'^export/wholesalelist', views.wholesaleList, name='wholesale_list'),
	url(r'^export/retaillist', views.retailList, name='retail_list'),
	#EXPORTER
	url(r'^export/shopify', views.shopifyExport, name='shopify_csv'),
	url(r'^export/retail', views.retailExport, name='retail_csv'),
]