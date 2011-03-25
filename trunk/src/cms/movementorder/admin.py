from django.contrib import admin
from movementorder.models import MovementOrder
from movementorder.models import MOParticipant

admin.site.register(MovementOrder)
admin.site.register(MOParticipant)