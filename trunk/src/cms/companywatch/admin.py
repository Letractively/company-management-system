from django.contrib import admin
from companywatch.models import WatchBill
from companywatch.models import AcYear
from companywatch.models import AcWatch
from companywatch.models import Watch
from companywatch.models import LogBook
from companywatch.models import LogEntry 

admin.site.register(AcYear)
admin.site.register(AcWatch)
admin.site.register(WatchBill)
admin.site.register(Watch)
admin.site.register(LogBook)
admin.site.register(LogEntry)