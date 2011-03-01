from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

namespace="weekends"

urlpatterns = patterns('weekends.views',

    url(r'^$', 'index', name = "weekendIndex"),
    (r'^/$', 'index'),
    (r'reqWeekend$', 'reqWeekend'),
    (r'cancelReqWeekend$', 'cancelReqWeekend'),
    url(r'view$', 'viewList', name = "viewList"),
    (r'view$', 'viewList'),

    url(r'admin$', 'admin', name = "weekendAdmin"),
    (r'saveWeekendCount$', 'saveWeekendCount'),

    url(r'co$', 'coApproval', name="coApproval"),
    (r'approveWeekend$', 'approveWeekend'),
    (r'denyWeekend$', 'denyWeekend'),
    (r'approveAllWeekends$', 'approveAllWeekends'),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
    (r'^admin/', include(admin.site.urls)),
)