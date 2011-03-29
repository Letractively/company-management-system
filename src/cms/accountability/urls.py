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
    url(r'selectEvent$', 'selectEvent', name = "selectEvent"),
    (r'reviewAttendance$', 'reviewAttendance'),
    url(r'cancelEvent$', 'cancelEvent', name = "cancelEvent"),
    (r'saveCancelEvent$', 'saveCancelEvent'),
    (r'makeDay$', 'makeDay'),

    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
     (r'^admin/', include(admin.site.urls)),
)

