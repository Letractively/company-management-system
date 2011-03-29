from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('mid.views',

    #General Options
    url(r'editPersonalInformation$', 'editPersonalInformation', name = "editPersonalInformation"),
    (r'savePersonalInformation$', 'savePersonalInformation'),
    url(r'viewDiscipline$', 'viewDiscipline', name = "viewDiscipline"),
    (r'viewDiscipline$', 'viewDiscipline'),
    url(r'selectPassChange$', 'selectPassChange', name = "passChange"),
    (r'passChange$', 'passChange'),

    #CC Options
    url(r'assignCOC$', 'assignCOC', name = "assignCOC"),
    (r'saveAssignCOC$', 'saveAssignCOC'),
    url(r'assignBillets$', 'assignBillets', name = "assignBillets"),
    (r'saveAssignBillets$', 'saveAssignBillets'),
    url(r'pendingApproval$', 'pendingApproval', name = "pendingApproval"),
    (r'specReqView$', 'specReqView'),
    (r'ormView$', 'ormView'),
    (r'approveChit$', 'approveChit'),

    #Admin options:
    url(r'selectUser$', 'selectUser', name = "selectUser"),
    (r'modifyUser$', 'modifyUser'),
    (r'saveUser$', 'saveUser'),
    (r'selectPassReset$', 'selectPassReset'),
    (r'passReset$', 'passReset'),
    
    #PMO options:
    url(r'PRTSat$', 'PRTSat', name = "PRTSat"),
    (r'savePRT$', 'savePRT'),
    
    #AC options:
    url(r'ACSat$', 'ACSat', name = "ACSat"),
    (r'saveAC$', 'saveAC'),
    
    #FLT options:
    url(r'roomAssignment$', 'roomAssignment', name = "roomAssignment"),
    (r'saveRoomAssignment$', 'saveRoomAssignment'),
    url(r'changeCompanyRoom$', 'changeCompanyRoom', name = "changeCompanyRoom"),
    (r'saveChangeCompanyRoom$', 'saveChangeCompanyRoom'),
    
    #A/C Options
    url(r'enterDiscipline$', 'enterDiscipline', name = "enterDiscipline"),
    (r'saveDiscipline$', 'saveDiscipline'),
    url(r'enterProbation$', 'enterProbation', name = "enterProbation"),
    (r'saveProbation$', 'saveProbation'),
    url(r'assessDiscipline$', 'assessDiscipline', name = "assessDiscipline"),
    (r'updateDiscipline$', 'updateDiscipline'),
    
    #CO options
    url(r'appointCC$', 'appointCC', name = "appointCC"),
    (r'saveAppointCC$', 'saveAppointCC'),
    url(r'changeCompany$', 'changeCompany', name = "changeCompany"),
    (r'saveChangeCompany$', 'saveChangeCompany'),
    
    url(r'logout$', 'logout', name="logout"),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
    (r'^admin/', include(admin.site.urls)),

)
