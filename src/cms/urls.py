from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # put url's to all the apps in this folder.
    #Initial login page
    #(r'^CMS/$', 'mid.views.login'),

    (r'^Accountability/', include('Accountability.urls')),
    (r'^Bravo_Inspection/', include('Bravo_Inspection.urls')),
    #(r'^Company_Blog/', include('Company_Blog.urls')),
    (r'^Company_Watch/', include('Company_Watch.urls')),
    (r'^Form1/',include('Form1.urls')),
    (r'^MID/', include('MID.urls')),    
        # this app may or may not need a url path.  i'm thinking no, but here it is for now - mlaws
    (r'^ORM/', include('ORM.urls')),
    (r'^Zero8/', include('Zero8.urls')),
    (r'^SpecialRequestChit/', include('SpecialRequestChit.urls')),
    (r'^Uniform_Inspection/', include('Uniform_Inspection.urls')),
    (r'^Weekends/', include('Weekends.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
     (r'^admin/', include(admin.site.urls)),
)
