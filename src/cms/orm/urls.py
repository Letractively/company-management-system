from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('orm.views',

    url(r'^$', 'ormDefault', name = "ormDefault"),
    (r'^/$', 'ormDefault'),
    
    url(r'addLeisure$', 'addLeisure', name = "addLeisure"),
    (r'saveLeisure$', 'saveLeisure'),
    url(r'addTravel$', 'addTravel', name = "addTravel"),
    (r'saveTravel$', 'saveTravel'),
    url(r'addRMP$', 'addRMP', name = "addRMP"),
    (r'saveRMP$', 'saveRMP'),
    
    (r'ormSubmit$', 'ormSubmit'),
    (r'ormView$', 'ormView'),

    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
     (r'^admin/', include(admin.site.urls)),
)
