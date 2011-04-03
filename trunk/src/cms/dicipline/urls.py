from django.conf.urls.defaults import *

# admin enabled
from django.contrib import admin
admin.autodiscover()

namespace="discipline"

urlpatterns = patterns('discipline.views',
                       
    #A/C Options
    url(r'enterDiscipline$', 'enterDiscipline', name = "enterDiscipline"),
    (r'saveDiscipline$', 'saveDiscipline'),
    url(r'enterProbation$', 'enterProbation', name = "enterProbation"),
    (r'saveProbation$', 'saveProbation'),
    url(r'assessDiscipline$', 'assessDiscipline', name = "assessDiscipline"),
    (r'updateDiscipline$', 'updateDiscipline'),

    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enabled the admin
     (r'^admin/', include(admin.site.urls)),
)
