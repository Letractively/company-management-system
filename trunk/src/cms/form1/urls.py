from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('form1.views',

    url(r'^$', 'form1', name = "form1"),
    (r'^/$', 'form1'),
    (r'form1View', 'form1View'),
    (r'form1Submit$', 'form1Submit'),
    url(r'form1Select$', 'form1Select', name = "form1Select"),
    (r'form1Save$', 'form1Save'),
    
    # Uncomment the admin/doc line below to enable admin documentation:    
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # enabled the admin
    (r'^admin/', include(admin.site.urls)),
)
