#cms urls.py
# Author: Laws, Rabe, Hatley, Harrison
# Editor: see above

from django.conf.urls.defaults import *
# admin enabled
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    #Initial login page    
    
    # put all of this under cms/mid now.
    (r'^$', 'mid.views.loginPage'),
    (r'^login$', 'mid.views.log_in'),

    # All the other module's pages
    (r'^accountability/', include('accountability.urls')),
    (r'^bravoinspection/', include('bravoinspection.urls')),
    #(r'^companyblog/', include('companyblog.urls')),
    (r'^companywatch/', include('companywatch.urls')),
    (r'^form1/',include('form1.urls')),
    (r'^mid/', include('mid.urls')),
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