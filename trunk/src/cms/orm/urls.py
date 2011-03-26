from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'orm', name = "orm"),
    (r'^/$', 'orm'),
    (r'ormSubmit$', 'ormSubmit'),
    (r'ormView$', 'ormView'),

    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
     (r'^admin/', include(admin.site.urls)),
)
