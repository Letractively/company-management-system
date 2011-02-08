from django.contrib import admin
from MID.models import Mid
from MID.models import Room
from MID.models import Billets

class ChoiceInline(admin.StackedInline):
    model = Billets
    extra = 0

class MidAdmin(admin.ModelAdmin):
    fieldsets = [
                 ('alpha:', {'fields':['alpha']}),
                 ('Name:', {'fields': ['LName']}),
                 ]
    inlines = [ChoiceInline]

admin.site.register(Mid, MidAdmin)
admin.site.register(Room)
admin.site.register(Billets)
