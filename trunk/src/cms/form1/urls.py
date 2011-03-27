from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('form1.views',

    url(r'^$', 'form1', name = "form1"),
    (r'^/$', 'form1'),
    (r'formOneView', 'formOneView'),
    (r'formOneSubmit$', 'formOneSubmit'),
    url(r'formOneSelect$', 'formOneSelect', name = "formOneSelect"),
    (r'formOneSave$', 'formOneSave'),
    
    # Uncomment the admin/doc line below to enable admin documentation:    
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # enabled the admin
    (r'^admin/', include(admin.site.urls)),
)
