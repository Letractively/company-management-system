from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

namespace = "accountability"

urlpatterns = patterns('accountability.views',

    url(r'^$', 'enterAttendance', name = "enterAttendance"),
    (r'^/$', 'enterAttendance'),
    #(r'reqWeekend$', 'reqWeekend'),
    #(r'cancelReqWeekend$', 'cancelReqWeekend'),
    #url(r'view$', 'viewList', name = "viewList"),
    #(r'view$', 'viewList'),

    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
     (r'^admin/', include(admin.site.urls)),
)