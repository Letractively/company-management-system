from django.db import models
# Create your models here.

class Bravo_Inspection(models.Model):
    #List of possible hits for a Bravo room inspection
    Inspector = models.ForeignKey("MID.Mid")
    Room = models.ForeignKey("MID.Room")
    When = models.DateTimeField('date inspected')
    Deck = models.BooleanField('Deck mopped clean, swept')
    Laundry = models.BooleanField('Excessive dirty laundry in locker/ No odor emanating')
    Mold = models.BooleanField('Mold in shower and/or shower curtain')
    Door = models.BooleanField('Door must be open at a 90 degree angle when the room is unoccupied')
    Electronics = models.BooleanField('All lights and electrical equipment is shut off')
    Dust = models.BooleanField('All surfaces clean and dusted')
    Bulkheads = models.BooleanField('Nothing hung from bulkhead, overheads, closets, racks, or doors')
    Racks = models.BooleanField('Racks neatly made with clean linen/pillow in place/ no blankets on rack')
    Furniture = models.BooleanField('No unauthorized furniture or appliances present (up to one non issued desk chair allowed per desk)')
    Felt = models.BooleanField('Protective felt pads on sled style chairs')
    Gear = models.BooleanField('No gear adrift')
    Con_Lockers = models.BooleanField('Confidential lockers locked')
    Blinds = models.BooleanField('Blinds at half mast and open')
    Boxes = models.BooleanField('All boxes and plastic containers are in closet or on shelves')
    Cork_board = models.BooleanField('Cork board/blotter/desk material appropriate and neatly arranged')
    Computer = models.BooleanField('Computer screensavers are appropriate and in good taste')
    Rugs = models.BooleanField('No rugs in room except shower mat, which must be clean')
    Mid_Regs = models.BooleanField('Mid Regs/ Uniform Regs and Honor Instruction binders in bracket')
    Shower = models.BooleanField('Shower walls, curtain, and deck clean')
    Medicine_cabinets = models.BooleanField('Medicine cabinet clean and neatly arranged')
    Bright_work = models.BooleanField('Brightwork work and mirros clean')
    Material_deficiencies = models.BooleanField('Material deficiencies documented on the room check-in sheet or updated on ZIDL')
    Rifles = models.BooleanField('All rifles and swords locked')
    def __unicode__(self):
        return self.Room.__str__() + " - " + self.When.__str__()