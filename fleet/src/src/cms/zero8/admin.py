from django.contrib import admin
from zero8.models import Zero8
from zero8.models import SignificantEvents
from zero8.models import Candidates
from zero8.models import Inspections
from zero8.models import OtherMaterialDiscrepancies
from zero8.models import InturmuralResults
from zero8.models import NextDayEvents

admin.site.register(Zero8)
admin.site.register(SignificantEvents)
admin.site.register(Candidates)
admin.site.register(Inspections)
admin.site.register(OtherMaterialDiscrepancies)
admin.site.register(InturmuralResults)
admin.site.register(NextDayEvents)