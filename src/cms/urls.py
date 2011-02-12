from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin



admin.autodiscover()

urlpatterns = patterns('',

    # put url's to all the apps in this folder.
    #Initial login page
    (r'^$', include('mid.urls')),
    (r'^login$', include('mid.urls')),

    (r'^accountability/', include('accountability.urls')),
    (r'^bravoinspection/', include('bravoinspection.urls')),
    #(r'^companyblog/', include('companyblog.urls')),
    (r'^companywatch/', include('companywatch.urls')),
    (r'^form1/',include('form1.urls')),
    (r'^mid/', include('mid.urls')),    
        # this app may or may not need a url path.  i'm thinking no, but here it is for now - mlaws
    (r'^orm/', include('orm.urls')),
    (r'^zero8/', include('zero8.urls')),
    (r'^specialrequestchit/', include('specialrequestchit.urls')),
    (r'^uniforminspection/', include('uniforminspection.urls')),
    (r'^weekends/', include('weekends.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
     (r'^admin/', include(admin.site.urls)),
)