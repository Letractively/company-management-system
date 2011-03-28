from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('companywatch.views',

    # put url's to all the apps in this folder.

    url(r'^$', 'AcYearView', name = 'AcYearView'),
    (r'^AcYearView$','AcYearView'),
    (r'^AcYearEdit$', 'AcYearEdit'),
    

    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
     (r'^admin/', include(admin.site.urls)),
)
