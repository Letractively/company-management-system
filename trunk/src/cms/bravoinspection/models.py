from django.db import models
# Create your models here.

class BravoInspection(models.Model):
    #List of possible hits for a Bravo room inspection
    inspector = models.ForeignKey("mid.Mid")
    room = models.ForeignKey("mid.Room")
    inspectionDate = models.DateTimeField('date inspected')
    deck = models.BooleanField('Deck mopped clean, swept')
    laundry = models.BooleanField('Excessive dirty laundry in locker/ No odor emanating')
    mold = models.BooleanField('Mold in shower and/or shower curtain')
    door = models.BooleanField('Door must be open at a 90 degree angle when the room is unoccupied')
    electronics = models.BooleanField('All lights and electrical equipment is shut off')
    dust = models.BooleanField('All surfaces clean and dusted')
    bulkheads = models.BooleanField('Nothing hung from bulkhead, overheads, closets, racks, or doors')
    racks = models.BooleanField('Racks neatly made with clean linen/pillow in place/ no blankets on rack')
    furniture = models.BooleanField('No unauthorized furniture or appliances present (up to one non issued desk chair allowed per desk)')
    felt = models.BooleanField('Protective felt pads on sled style chairs')
    gear = models.BooleanField('No gear adrift')
    conLockers = models.BooleanField('Confidential lockers locked')
    blinds = models.BooleanField('Blinds at half mast and open')
    boxes = models.BooleanField('All boxes and plastic containers are in closet or on shelves')
    corkBoard = models.BooleanField('Cork board/blotter/desk material appropriate and neatly arranged')
    computer = models.BooleanField('Computer screensavers are appropriate and in good taste')
    rugs = models.BooleanField('No rugs in room except shower mat, which must be clean')
    midRegs = models.BooleanField('Mid Regs/ Uniform Regs and Honor Instruction binders in bracket')
    shower = models.BooleanField('Shower walls, curtain, and deck clean')
    medicineCabinets = models.BooleanField('Medicine cabinet clean and neatly arranged')
    brightWork = models.BooleanField('Brightwork work and mirros clean')
    materialDeficiencies = models.BooleanField('Material deficiencies documented on the room check-in sheet or updated on ZIDL')
    rifles = models.BooleanField('All rifles and swords locked')
    def __unicode__(self):
        return self.Room.__str__() + " - " + self.When.__str__()