from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='friardata'),
	url(r'^wholesalelist/', views.wholesale_list, name='wholesalelist'),
	url(r'^retaillist/', views.retail_list, name='retaillist'),
	url(r'^shopify/', views.shopify_export, name='shopify'),
]