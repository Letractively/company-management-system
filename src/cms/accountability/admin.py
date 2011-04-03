from django.contrib import admin
from accountability.models import Event
from accountability.models import Attendance
from mid.models import Absence

admin.site.register(Event)
admin.site.register(Attendance)
admin.site.register(Absence)