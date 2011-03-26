from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('mid.views',

    #Admin options:
    url(r'selectUser$', 'selectUser', name = "selectUser"),
    (r'modifyUser$', 'modifyUser'),
    (r'saveUser$', 'saveUser'),
    
    url(r'selectPassChange$', 'selectPassChange', name = "passChange"),
    (r'passChange$', 'passChange'),
    (r'selectPassReset$', 'selectPassReset'),
    (r'passReset$', 'passReset'),
    
    #PMO options:
    url(r'PRTSat$', 'PRTSat', name = "PRTSat"),
    (r'savePRTSat$', 'savePRTSat'),
    
    #A/C Options
    url(r'enterDiscipline$', 'enterDiscipline', name = "enterDiscipline"),
    (r'saveDiscipline$', 'saveDiscipline'),
    url(r'enterProbation$', 'enterProbation', name = "enterProbation"),
    (r'saveProbation$', 'saveProbation'),
    url(r'assessDiscipline$', 'assessDiscipline', name = "assessDiscipline"),
    (r'updateDiscipline$', 'updateDiscipline'),
    
    # put url's to all the apps in this folder.

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
    (r'^admin/', include(admin.site.urls)),

)
