from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

namespace="movementorder"

urlpatterns = patterns('movementorder.views',

    url(r'^$', 'MO', name = "MO"),
    (r'^/$', 'MO'),
    (r'checkOutMO$', 'checkOutMO'),
    (r'checkInMO$', 'checkInMO'),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
    (r'^admin/', include(admin.site.urls)),
)