#cms urls.py
# Author: Laws, Rabe, Hatley, Harrison
# Editor: see above

from django.conf.urls.defaults import *
# admin enabled

from django.contrib import admin
from django.views.static import *
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    
    #Initial login page    
    
    #Do NOT "fix" logIn/logOut to be login/logout, it'll break stuff

    url(r'^$', 'mid.views.loginPage', name = "base"),
    
    # We do not want any functionality at /cms.  We only want functionality at /cms/
    #(r'^/$', 'mid.views.loginPage'),
    
    
    (r'^login$', 'mid.views.logIn'),
    (r'^logout$', 'mid.views.logOut'),
    url(r'^switchboard$', 'mid.views.renderSwitchboard', name = "switchboard"),

    
    (r'^mid/', include('mid.urls', namespace="mid", app_name="mid")),
    
    #Chits/Paperwork
    (r'^formOne/',include('form1.urls')),
    (r'^medchits/', include('medchits.urls')),
    (r'^specReq/', include('specialrequestchit.urls')),
    (r'^ORM/', include('orm.urls')),

    #Inspections
    (r'^bIns/', include('bravoinspection.urls')),
    (r'^uIns/', include('uniforminspection.urls')),
    
    # All the other module's pages
    #(r'^accountability/', include('accountability.urls')),
    #(r'^companyblog/', include('companyblog.urls')),
    #(r'^companywatch/', include('companywatch.urls')),
    #(r'^zero8/', include('zero8.urls')),
    
    (r'^weekends/', include('weekends.urls')),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
    (r'^admin/', include(admin.site.urls)),
    
    # static content
    (r'media/(?P<path>.*)$','django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}),
)