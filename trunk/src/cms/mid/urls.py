from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('mid.views',

    (r'^selectUser$', 'selectUser'),
    (r'^modifyUser$', 'modifyUser'),
    (r'^saveUser$', 'saveUser'),
    (r'^selectPassReset$', 'selectPassReset'),
    (r'^passReset$', 'passReset'),
    (r'^selectPassChange$', 'selectPassChange'),
    (r'^passChange$', 'passChange'),
    
    # put url's to all the apps in this folder.

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
    (r'^admin/', include(admin.site.urls)),

)
