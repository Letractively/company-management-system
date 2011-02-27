from django.db import models

# Create your models here.
class UniformInspection(models.Model):
    #List of possible hits for a uniform inspection
    inspectorAlpha = models.CharField(max_length=6)
    mid = models.ForeignKey("mid.Mid")
    inspectionDate = models.DateField()

    # int field for the score
    score = models.IntegerField(null=True)
    
    # i think "pass" is a reserved term in python, so this is the fail block, passing by default.
    fail = models.BooleanField(null=True).default=False
    
    missingItems = models.BooleanField('No missing uniform items')
    appearance = models.BooleanField('Uniform Appearance(stains/wrinkles)')
    groomingShave = models.BooleanField('Hair/Grooming: Shave/Sideburns')
    groomingLength = models.BooleanField('Hair/Grooming: Proper Length')
    groomingAppearance = models.BooleanField('Hair/Grooming: Neat Appearance')
    creasesPresent = models.BooleanField('Creases present')
    shinedShoes = models.BooleanField('Shined Shoes')
    ribbons = models.BooleanField('Ribbons/ Nametag appearance/ placement')
    IPs = models.BooleanField('No IP')
    dust = models.BooleanField('No Dust')
    coverDirtRing = models.BooleanField('Cover: dirt ring/dirty/marks')
    coverCleanBill = models.BooleanField('Cover: clean bill')
    shirtUndershirt = models.BooleanField('Shirt: undershirt not showing')
    shirtProperTie = models.BooleanField('Shirt: proper tie knot/neck tab button buttoned')
    shirtInsigniaPlacement = models.BooleanField('Shirt: insignia placement')
    beltBuckleTip = models.BooleanField('Belt: buckle/tip scratches/dirty')
    gigLine = models.BooleanField('Gig-line straight')
    trousersProperLength = models.BooleanField('Trousers: proper length')
    IDProperlyDisplayed = models.BooleanField('ID displayed (if inside)')
    other = models.TextField('General appearance')
    
    def __unicode__(self):
        return self.mid + " - " + self.DateTime
