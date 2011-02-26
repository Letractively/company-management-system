from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('weekends.views',


    (r'$', 'index'),
    (r'reqWeekend$', 'reqWeekend'),
    (r'cancelReqWeekend$', 'cancelReqWeekend'),
    (r'view$', 'viewList'),

    (r'admin$', 'admin'),
    (r'saveWeekendCount$', 'saveWeekendCount'),

    (r'co$', 'coApproval'),
    (r'approveWeekend$', 'approveWeekend'),
    (r'denyWeekend$', 'denyWeekend'),
    (r'approveAllWeekends$', 'approveAllWeekends'),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
    (r'^admin/', include(admin.site.urls)),
)