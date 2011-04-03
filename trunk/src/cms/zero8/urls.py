from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

namespace = "zero8"

urlpatterns = patterns('zero8.views',

    url(r'createSignificantEvent', 'createSignificantEvent', name = "createSignificantEvent"),
    (r'saveSignificantEvent$', 'saveSignificantEvent'),
    url(r'candidates', 'candidates', name = "candidates"),
    (r'saveCandidate$', 'saveCandidate'),
    (r'removeCandidate$', 'removeCandidate'),
    url(r'viewReport$', 'viewReport', name = "viewReport"),


    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
     (r'^admin/', include(admin.site.urls)),
)

