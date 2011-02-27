from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('form1.views',

    url(r'^$', 'formOne', name = "formOne"),
    (r'^/$', 'formOne'),
    (r'FormOneView', 'FormOneView'),
    (r'formOneSubmit$', 'formOneSubmit'),
    
    # Uncomment the admin/doc line below to enable admin documentation:    
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # enabled the admin
    (r'^admin/', include(admin.site.urls)),
)
