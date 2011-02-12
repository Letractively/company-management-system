from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('form1.views',

    # put url's to all the apps in this folder.

    # (r'^cms/', include('cms.foo.urls')),
    (r'^form1/', 'createNewForm1'),
    

    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
     (r'^admin/', include(admin.site.urls)),
)
