#cms urls.py
# Author: Laws, Rabe, Hatley, Harrison
# Editor: see above

from django.conf.urls.defaults import *
# admin enabled

from django.contrib import admin
from django.views.static import *
from django.conf import settings
admin.autodiscover()

namespace="cms"

urlpatterns = patterns('',
    
    #Do NOT "fix" logIn/logOut to be login/logout, it'll break stuff

    url(r'^$', 'mid.views.loginPage', name = "base"),
    
    # We do not want any functionality at /cms.  We only want functionality at /cms/
    #(r'^/$', 'mid.views.loginPage'),
    
    
    (r'^login$', 'mid.views.logIn'),
    url(r'^logout$', 'mid.views.logOut', name="logout"),
    url(r'^switchboard$', 'mid.views.renderSwitchboard', name = "switchboard"),
    
    (r'^mid/', include('mid.urls', namespace="mid", app_name="mid")),
    
    #Chits/Paperwork
    (r'^form1/',include('form1.urls', namespace="form1", app_name="form1")),
    (r'^medchits/', include('medchits.urls', namespace="medchits", app_name="medchits")),
    (r'^specReq/', include('specialrequestchit.urls', namespace="specialrequestchit", app_name="specialrequestchit")),
    (r'^ORM/', include('orm.urls', namespace="orm", app_name="orm")),

    #Inspections
    (r'^bIns/', include('bravoinspection.urls', namespace="bIns", app_name="bravoinspection")),
    (r'^uIns/', include('uniforminspection.urls', namespace="uIns", app_name="uniforminspection")),
    
    # All the other module's pages
    #(r'^companyblog/', include('companyblog.urls')),
    (r'^companywatch/', include('companywatch.urls', namespace="companywatch", app_name="companywatch")),
    
    (r'^accountability/', include('accountability.urls', namespace = "accountability", app_name = "accountability")),
    (r'^weekends/', include('weekends.urls', namespace="weekends", app_name="weekends")),
    (r'^discipline/', include('discipline.urls', namespace="discipline", app_name="discipline")),
    (r'^movementOrders/', include('movementorder.urls', namespace="movementorder", app_name="movementorder")),
    (r'^zero8/', include('zero8.urls', namespace = "zero8", app_name = "zero8")),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
    (r'^admin/', include(admin.site.urls)),
    
    # static content
    (r'media/(?P<path>.*)$','django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}),
)
