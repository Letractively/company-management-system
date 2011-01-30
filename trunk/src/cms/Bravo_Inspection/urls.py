from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # put url's to all the apps in this folder.

    # (r'^cms/', include('cms.foo.urls')),
    (r'^Bravo_Inspection/(?P<poll_id>\d+)/enter/$', 'Bravo_Inspection.views.enter'),
    (r'^Bravo_Inspection/(?P<poll_id>\d+)/results/$', 'Bravo_Inspection.views.review'),

    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
     (r'^admin/', include(admin.site.urls)),
)
