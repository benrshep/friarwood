from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^winelist/', views.pdf_creator, name='winelist'),
	url(r'^shopify/', views.shopify_export, name='shopify'),
]