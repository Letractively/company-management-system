from django.db import models

# Create your models here.
class UniformInspection(models.Model):
    #List of possible hits for a uniform inspection
    Inspector = models.ForeignKey("MID.Mid")
    Room = models.ForeignKey("MID.Room")
    DateTime = models.DateTimeField()
    Missing_items = models.BooleanField('No missing uniform items')
    Appearance = models.BooleanField('Uniform Appearance(stains/wrinkles)')
    Grooming_Shave = models.BooleanField('Hair/Grooming: Shave/Sideburns')
    Grooming_Length = models.BooleanField('Hair/Grooming: Proper Length')
    Grooming_Appearance = models.BooleanField('Hair/Grooming: Neat Appearance')
    Creases_present = models.BooleanField('Creases present')
    Shined_shoes = models.BooleanField('Shined Shoes')
    Ribbons = models.BooleanField('Ribbons/ Nametag appearance/ placement')
    IPs = models.BooleanField('No IP')
    Dust = models.BooleanField('No Dust')
    Cover_dirt_ring = models.BooleanField('Cover: dirt ring/dirty/marks')
    Cover_clean_bill = models.BooleanField('Cover: clean bill')
    Shirt_undershirt = models.BooleanField('Shirt: undershirt not showing')
    Shirt_proper_tie = models.BooleanField('Shirt: proper tie knot/neck tab button buttoned')
    Shirt_insignia_placement = models.BooleanField('Shirt: insignia placement')
    Belt_buckle_tip = models.BooleanField('Belt: buckle/tip scratches/dirty')
    Gig_line = models.BooleanField('Gig-line straight')
    Trousers_proper_length = models.BooleanField('Trousers: proper length')
    ID_properly_displayed = models.BooleanField('ID displayed (if inside)')
    Other = models.TextField('General appearance')
    def __unicode__(self):
        return self.Room + " - " + self.DateTime
