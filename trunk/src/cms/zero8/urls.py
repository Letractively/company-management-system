from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

namespace = "zero8"

urlpatterns = patterns('zero8.views',

    url(r'createSignificantEvent', 'createSignificantEvent', name = "createSignificantEvent"),
    (r'saveSignificantEvent$', 'saveSignificantEvent'),
    url(r'candidates', 'candidates', name = "candidates"),
    (r'saveCandidate$', 'saveCandidate'),
    (r'removeCandidate$', 'removeCandidate'),
    url(r'dutySectionMuster$', 'dutySectionMuster', name = "dutySectionMuster"),
    (r'saveDutySectionMuster$', 'saveDutySectionMuster'),
    url(r'bedCheck$', 'bedCheck', name = "bedCheck"),
    (r'saveBedCheck$', 'saveBedCheck'),
    url(r'studyHour$', 'studyHour', name = "studyHour"),
    (r'saveStudyHour$', 'saveStudyHour'),
    url(r'BAC$', 'BAC', name = "BAC"),
    (r'saveB$', 'saveB'),
    url(r'restrictees$', 'restrictees', name = "restrictees"),
    (r'saveRestrictees$', 'saveRestrictees'),
    (r'selectReport$', 'selectReport'),
    url(r'setFPC$', 'setFPC', name = "setFPC"),
    (r'saveFPC$', 'saveFPC'),
    url(r'addIntramurals$', 'addIntramurals', name = "addIntramurals"),
    (r'saveIntramurals$', 'saveIntramurals'),
    url(r'addNDE$', 'addNDE', name = "addNDE"),
    (r'saveNDE$', 'saveNDE'),
    
    url(r'viewReport$', 'viewReport', name = "viewReport"),


    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
     (r'^admin/', include(admin.site.urls)),
)

