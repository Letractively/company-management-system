#uniforminspection models.py
# Author: Michael Harrison
# Editor: Michael Laws


from django.db import models

# Create your models here.
class UniformInspection(models.Model):
    mid = models.ForeignKey("mid.Mid")
    inspector = models.ForeignKey("mid.Mid", related_name='+')
    inspectionDate = models.DateField()

    # int field for the score
    score = models.IntegerField(null=True)
    
    # i think "pass" is a reserved term in python, so this is the fail block, passing by default.
    fail = models.BooleanField(null=True).default=False
    
    #List of possible hits for a uniform inspection
    groomingShave = models.BooleanField('Grooming: Unshaved')
    groomingLength = models.BooleanField('Grooming: Hair out of regs')
    groomingAppearance = models.BooleanField('Grooming: appearance is not neat')
    
    missingItems = models.BooleanField('Uniform: Missing articles')
    appearance = models.BooleanField('Uniform: Poor appearance')
    IPs = models.BooleanField('Uniform: IP-s present')
    dust = models.BooleanField('Uniform: Dusty')
       
    coverDirtRing = models.BooleanField('Cover: Dirty')
    coverCleanBill = models.BooleanField('Cover: Scratched bill')
    
    ribbons = models.BooleanField('Shirt: ribbons/nametag poorly placed/tarnished') 
    shirtInsigniaPlacement = models.BooleanField('Shirt: Collar devices poorly placed/tarnished')
    shirtProperTie = models.BooleanField('Shirt: Improper tie knot/neck tab')
    IDProperlyDisplayed = models.BooleanField('Shirt: Improper ID placement')
    shirtUndershirt = models.BooleanField('Shirt: Showing undershirt')
    creasesPresent = models.BooleanField('Shirt: No creases')
    
    beltBuckleTip = models.BooleanField('Belt: Buckle scratched')
    gigLine = models.BooleanField('Belt: Poor gig-line')
    
    trousersProperLength = models.BooleanField('Trousers: Poor length/fit')
    
    shinedShoes = models.BooleanField('Shoes: No shine')
      
    other = models.TextField('General appearance')
    
    def __unicode__(self):
        return self.mid + " - " + self.inspectionDate.__str__()
