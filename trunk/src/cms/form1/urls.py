from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('form1.views',

    url(r'^$', 'form1', name = "form1"),
    (r'^/$', 'form1'),
    (r'form1Save$', 'form1Save'),
    (r'form1View', 'form1View'),
    
    # Uncomment the admin/doc line below to enable admin documentation:    
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # enabled the admin
    (r'^admin/', include(admin.site.urls)),
)
