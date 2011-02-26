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
    (r'^$', 'mid.views.loginPage'),
    (r'^login/$', 'mid.views.logIn'),
    (r'^logout/$', 'mid.views.logOut'),
    (r'^switchboard/$', 'mid.views.renderSwitchboard'),
    
    (r'^mid/$', include('mid.urls')),
    
    #Chits/Paperwork
    (r'^medchits/&', include('medchits.urls')),
    # All the other module's pages
    #(r'^accountability/', include('accountability.urls')),
    #(r'^bravoinspection/', include('bravoinspection.urls')),
    #(r'^companyblog/', include('companyblog.urls')),
    #(r'^companywatch/', include('companywatch.urls')),
    #(r'^form1/',include('form1.urls')),
    #(r'^orm/', include('orm.urls')),
    #(r'^zero8/', include('zero8.urls')),
    #(r'^specialrequestchit/', include('specialrequestchit.urls')),
    #(r'^uniforminspection/', include('uniforminspection.urls')),
    
    (r'^weekends/&', include('weekends.urls')),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
    (r'^admin/', include(admin.site.urls)),
    
    # static content
    (r'media/(?P<path>.*)$','django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}),
)