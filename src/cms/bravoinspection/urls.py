from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('bravoinspection.views',

    url(r'^$', 'bIns', name = "bIns"),
    (r'^/$', 'bIns'),
    (r'bInsView', 'bInsView'),
    (r'bInsSubmit$', 'bInsSubmit'),

    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
     (r'^admin/', include(admin.site.urls)),
)
