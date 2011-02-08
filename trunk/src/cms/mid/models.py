from django.db import models

# Create your models here.
BILLET_CHOICES = (
    ('CC','Company Commander'),
    ('XO','Executive Officer'),
    ('HA','Honor Advisor'),
    ('OPS','Operations Officer'),
    ('ADJ','Adjutant'),
    ('PMO','Physical Mission Officer'),
    ('AC','Academics Officer'),
    ('SAF','Safety Officer'),
    ('A/C','Aptitiude/Conduct Officer'),
    ('ADEO','ADEO'),
    ('ATFP','ATFP'),
    ('TRN','Training Officer'),
    ('1LT','1st LT'),
    ('ADM','Administrative Officer'),
    ('PRO','Protocol Officer'),
    ('WRD','Wardroom'),
    ('DRL','Drill Officer'),
    ('SAVI','SAVI'),
    ('CMEO','CMEO'),
    ('FIN','Financial Officer'),
    ('1SGT','1st Sergeant'),
    ('TRNS','Training Sgt'),
    ('DRLS','Drill Sgt'),
    ('ADMC','Admin Chief'),
    ('MISLO','MISLO'),
    ('PC','Platoon CDR'),
    ('SL','Squad Leader'),
    ('PLTS','Platoon Sgt'),
    ('OOC','Out of Company'),
    )
PLT_CHOICES = (
    ('1','1st Platoon'),
    ('2','2nd Platoon'),
    ('3','3rd Platoon'),
    ('4','4th Platoon'),
    ('O','Out of Company'),
    ('S','Company Staff'),
    )
SQD_CHOICES = (
    ('1','1st Squad'),
    ('2','2nd Squad'),
    ('3','3rd Squad'),
    ('O','Out of Company'),
    ('S','Company Staff'),
    )
class Room(models.Model):
    roomNumber = models.CharField(max_length=4,primary_key=True)
    maxOccupants = models.CharField(max_length=1)
    def __unicode__(self):
        return self.RoomNumber
    
class Mid(models.Model):
    alpha = models.CharField(max_length=6,primary_key=True)
    LName = models.CharField(max_length=30)
    mName = models.CharField(max_length=3)
    fName = models.CharField(max_length=30)
    platoon = models.CharField(max_length=1, choices=PLT_CHOICES,null=True)
    squad = models.CharField(max_length=1, choices=SQD_CHOICES,null=True)
    roomNumber = models.ForeignKey(Room,null=True)
    phoneNumber = models.CharField(max_length=10,null=True)
    weekends = models.IntegerField(null=True)
    weekendsComment = models.CharField(max_length=50)
    acSAT = models.BooleanField(null=True).default=True
    PRTSat = models.BooleanField(null=True).default=True
    CQPR = models.DecimalField(max_digits=4, decimal_places=2,null=True)
    SQPR = models.DecimalField(max_digits=4, decimal_places=2,null=True)
    performanceGrade = models.CharField(max_length=1,null=True)
    conductGrade = models.CharField(max_length=1,null=True)
    PRT = models.DecimalField(max_digits=3, decimal_places=2,null=True)
    def __unicode__(self):
        return self.L_Name + ", " + self.F_Name + " " + self.MI_Name + " - " + self.Alpha
    
class Billets(models.Model):
    mid = models.ForeignKey(Mid)
    billet = models.CharField(max_length=4,choices=BILLET_CHOICES)
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    evaluation = models.TextField(null=True)
    current = models.NullBooleanField()
    def __unicode__(self):
        return self.Billet
    
class Absences(models.Model):
    zero8 = models.ForeignKey("zero8.Zero8")
    name = models.ForeignKey(Mid)
    authorized = models.BooleanField()
    description = models.CharField(max_length=20)
    adminNote = models.CharField(max_length=90)
    REASON_CHOICES = (
                     ('AA','Authorized Absence'),
                     ('UA','Unauthorized Absence'),
                     ('WE','Weekend'),
                     ('MO','Movement Order'),
                     )
    reason = models.CharField(max_length=2,choices=REASON_CHOICES)    
 
class Discipline(models.Model):
    mid = models.ForeignKey(Mid)
    conductHonor = models.BooleanField()
    dateOffence = models.DateField()
    startDate = models.DateField()
    daysAwarded = models.IntegerField()
    toursAwarded = models.IntegerField()
    toursRemaining = models.IntegerField()
    adminNotes = models.CharField(max_length=90)
    checked = models.DateField()
    
class Separations(models.Model):
    zero8 = models.ForeignKey("zero8.Zero8")
    mid = models.ForeignKey("Mid")
    pending = models.BooleanField()
    adminNote = models.CharField(max_length=90)
    
class Probation(models.Model):
    mid = models.ForeignKey(Mid)
    startDate = models.DateField()
    daysAwarded = models.IntegerField()
    description = models.CharField(max_length=50)