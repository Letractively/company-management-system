from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

namespace = "specialrequestchit"

urlpatterns = patterns('specialrequestchit.views',

    url(r'^$', 'specReq', name = "specReq"),
    (r'^/$', 'specReq'),
    (r'specReqSubmit$', 'specReqSubmit'),
    (r'specReqView$', 'specReqView'),

    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
     (r'^admin/', include(admin.site.urls)),
)
