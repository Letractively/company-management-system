from django.contrib import admin
from mid.models import Mid
from mid.models import Room
from mid.models import Billets


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
apt