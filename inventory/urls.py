from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$/pdf/', views.pdf_creator, name='pdf'),
]