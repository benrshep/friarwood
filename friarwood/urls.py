from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
	url(r'^export/', include('inventory.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('admin:index')))
]