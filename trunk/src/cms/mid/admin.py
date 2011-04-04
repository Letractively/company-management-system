from django.contrib import admin
from mid.models import Mid
from mid.models import Room
from mid.models import Billet
from mid.models import Grade
from mid.models import PRT


class ChoiceInline(admin.StackedInline):
    model = Billet
    extra = 0

class MidAdmin(admin.ModelAdmin):
    search_fields = ['fName','LName','alpha']
    list_filter = ['company']

admin.site.register(Mid, MidAdmin)
admin.site.register(Room)
admin.site.register(Billet)
admin.site.register(Grade)
admin.site.register(PRT)