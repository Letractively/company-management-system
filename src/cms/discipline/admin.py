from django.contrib import admin
from discipline.models import Restriction
from discipline.models import Tours
from discipline.models import Separation
from discipline.models import Probation

admin.site.register(Restriction)
admin.site.register(Tours)
admin.site.register(Separation)
admin.site.register(Probation)
