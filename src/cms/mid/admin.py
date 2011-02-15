from django.contrib import admin
from mid.models import Mid
from mid.models import Room
from mid.models import Billet


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