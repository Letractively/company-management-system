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
    RoomNumber = models.CharField(max_length=4,primary_key=True)
    maxOccupants = models.CharField(max_length=1)
    def __unicode__(self):
        return self.RoomNumber
    
class Mid(models.Model):
    Alpha = models.CharField(max_length=6,primary_key=True)
    L_Name = models.CharField(max_length=30)
    MI_Name = models.CharField(max_length=3)
    F_Name = models.CharField(max_length=30)
    PLT = models.CharField(max_length=1, choices=PLT_CHOICES,null=True)
    SQD = models.CharField(max_length=1, choices=SQD_CHOICES,null=True)
    RoomNumber = models.ForeignKey(Room,null=True)
    PhoneNumber = models.CharField(max_length=10,null=True)
    Weekends = models.IntegerField(null=True)
    AcSAT = models.BooleanField(null=True).default=True
    PRTSAT = models.BooleanField(null=True).default=True
    CQPR = models.DecimalField(max_digits=4, decimal_places=2,null=True)
    SQPR = models.DecimalField(max_digits=4, decimal_places=2,null=True)
    PerfGrade = models.CharField(max_length=1,null=True)
    ConductGrade = models.CharField(max_length=1,null=True)
    PRT = models.DecimalField(max_digits=3, decimal_places=2,null=True)
    def __unicode__(self):
        return self.L_Name + ", " + self.F_Name + " " + self.MI_Name + " - " + self.Alpha
    
class Billets(models.Model):
    mid = models.ForeignKey(Mid)
    Billet = models.CharField(max_length=4,choices=BILLET_CHOICES)
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    Evaluation = models.TextField(null=True)
    Current = models.NullBooleanField()
    def __unicode__(self):
        return self.Billet
    
class Absencs(models.Model):
    Zero8 = models.ForeignKey(Zero8)
    Name = models.ForeignKey(Mid)
    Authorized = models.BooleanField()
    Description = models.CharField(max_length=20)
    Admin_Note = models.CharField(max_length=90)
    REASON_CHOICES = (
                     ('AA','Authorized Absence'),
                     ('UA','Unauthorized Absence'),
                     ('WE','Weekend'),
                     ('MO','Movement Order'),
                     )
    Reason = models.CharField(max_length=2,choices=REASON_CHOICES)    
 
class Disipline(models.Model):
    Mid = models.ForeignKey(Mid)
    Conduct_Honor = models.BooleanField()
    Date_Offence = models.DateField()
    Restriction_Days_Awarded = models.IntegerField()
    Restriction_Days_Remaining = models.IntegerField()
    Tours_Awarded = models.IntegerField()
    Tours_Remaining = models.IntegerField()
    Admin_Notes = models.CharField(max_length=90)
    Checked = models.DateField()
    
class Separations(models.Model):
    Zero8 = models.ForeignKey(Zero8)
    Mid = models.ForeignKey("MID.Mid")
    Pending = models.BooleanField()
    Admin_Note = models.CharField(max_length=90)
    
class Probation(models.Model):
    mid = models.ForeignKey(Mid)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(maxlength=50)