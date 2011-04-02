from django.contrib import admin
from mid.models import Mid
from mid.models import Room
from mid.models import Billet
from mid.models import Grade
from mid.models import PRT
from mid.models import Absence


class ChoiceInline(admin.StackedInline):
    model = Billet
    extra = 0

class MidAdmin(admin.ModelAdmin):
    fieldsets = [
                 ('alpha:', {'fields':['alpha']}),
                 ('Name:', {'fields': ['LName']}),
                 ]
    inlines = [ChoiceInline]

admin.site.register(Mid)
admin.site.register(Room)
admin.site.register(Billet)
admin.site.register(Grade)
admin.site.register(PRT)
admin.site.register(Absence)