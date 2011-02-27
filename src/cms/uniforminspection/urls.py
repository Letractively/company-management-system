from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('uniforminspection.views',

    url(r'^$', 'uIns', name = "uIns"),
    (r'^/$', 'uIns'),
    (r'uInsView', 'uInsView'),
    (r'uInsSubmit$', 'uInsSubmit'),

    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
     (r'^admin/', include(admin.site.urls)),
)
