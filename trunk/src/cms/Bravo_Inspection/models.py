from django.db import models
from MID import Mid
# Create your models here.

class Brovo_Inspection(models.Model):
    #List of possible hits for a Brovo room inspection
    Inspector = models.ForeignKey(Mid)
    Room = models.ForeignKey(Room)
    Deck = models.BooleanField()
    Laundry = models.BooleanField()
    Mold = models.BooleanField()
    Door = models.BooleanField()
    Electronics = models.BooleanField()
    Dust = models.BooleanField()
    Bulkheads = models.BooleanField()
    Racks = models.BooleanField()
    Furniture = models.BooleanField()
    Felt = models.BooleanField()
    Gear = models.BooleanField()
    Con_Lockers = models.BooleanField()
    Blinds = models.BooleanField()
    Boxes = models.BooleanField()
    Cork_board = models.BooleanField()
    Computer = models.BooleanField()
    Rugs = models.BooleanField()
    Mid_Regs = models.BooleanField()
    Shower = models.BooleanField()
    Medicine_cabinets = models.BooleanField()
    Bright_work = models.BooleanField()
    Material_deficiencies = models.BooleanField()
    Rifles = models.BooleanField()