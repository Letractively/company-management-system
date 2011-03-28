from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

namespace = "accountability"

urlpatterns = patterns('accountability.views',

    url(r'^$', 'enterAttendance', name = "enterAttendance"),
    (r'^/$', 'enterAttendance'),
    (r'saveAttendance$', 'saveAttendance'),
    url(r'createEvent', 'createEvent', name = "createEvent"),
    (r'saveEvent$', 'saveEvent'),

    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
     (r'^admin/', include(admin.site.urls)),
)