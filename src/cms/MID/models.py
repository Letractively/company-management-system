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
    )
SQD_CHOICES = (
    ('1','1st Squad'),
    ('2','2nd Squad'),
    ('3','3rd Squad'),
    )
ROOM_CHOICES = (
    #Make in to Class
    ('6302','6302-2'),
    ('6303','6303-3'),
    ('6304','6304-3'),
    ('6305','6305-2'),
    ('6306','6306-2'),
    ('6307','6307-3'),
    ('6308','6308-4'),
    ('6309','6309-2'),
    ('6311','6311-3'),
    ('6314','6314-2'),
    ('6315','6315-3'),
    ('6316','6316-3'),
    ('6317','6317-3'),
    ('6318','6318-3'),
    ('6319','6319-3'),
    ('6320','6320-3'),
    ('6322','6322-2'),
    ('6323','6323-3'),
    ('6329','6329-3'),
    ('6402','6402-3'),
    ('6403','6403-2'),
    ('6404','6404-2'),
    ('6405','6405-2'),
    ('6406','6406-2'),
    ('6407','6407-2'),
    ('6408','6408-3'),
    ('6409','6409-2'),
    ('6411','6411-4'),
    ('6413','6413-2'),
    ('6414','6414-2'),
    ('6415','6415-2'),
    ('6416','6416-2'),
    ('6417','6417-2'),
    ('6418','6418-2'),
    ('6419','6419-2'),
    ('6420','6420-2'),
    ('6421','6421-3'),
    ('6425','6425-4'),
    ('6428','6428-2'),
    ('6429','6429-2'),
    ('6430','6430-2'),
    ('6431','6431-2'),
    ('6432','6432-2'),
    ('6433','6433-2'),
    ('6434','6434-2'),
    ('6435','6435-2'),
    ('6437','6437-2'),
    ('6438','6438-3'),
    ('6439','6439-2'),
    ('6440','6440-2'),
    ('6441','6441-4'),
    ('6443','6443-2'),
    ('6444','6444-2'),
    ('6445','6445-2'),
    ('6446','6446-2'),
    ('6455','6455-4'),
    ('6459','6459-2'),
    ('6460','6460-3'),
    ('6461','6461-2'),
    ('6462','6462-2'),
    ('6463','6463-2'),
    ('6464','6464-2'),
    ('6466','6466-3'),
    )

class Room(models.Model):
    RoomNumber = models.CharField(max_length=4,primary_key=True,choices=ROOM_CHOICES)
    maxOccupants = models.CharField(max_length=1)
    
class Mid(models.Model):
    Alpha = models.CharField(max_length=6,primary_key=True)
    L_Name = models.CharField(max_length=30)
    MI_Name = models.CharField(max_length=3)
    F_Name = models.CharField(max_length=30)
    PLT = models.CharField(max_length=1, choices=PLT_CHOICES)
    SQD = models.CharField(max_length=1, choices=SQD_CHOICES)
    #Billets = models.CharField(max_length=4, choices=BILLET_CHOICES) //this needs to be its own class because of inharitance
    RoomNumber = models.ForeignKey(Room)
    PhoneNumber = models.CharField(max_length=10)
    Weekends = models.IntegerField()
    AcSAT = models.BooleanField().default=True
    PRTSAT = models.BooleanField().default=True
    CQPR = models.DecimalField(max_digits=4, decimal_places=2)
    SQPR = models.DecimalField(max_digits=4, decimal_places=2)
    PerfGrade = models.CharField(max_length=1)
    ConductGrade = models.CharField(max_length=1)
    PRT = models.IntegerField(max_length=3)
    
class Billets(models.Model):
    mid = models.ForeignKey(Mid)
    Billet = models.CharField(max_length=4,choices=BILLET_CHOICES)
    startDate = models.DateField()
    endDate = models.DateField()
    Evaluation = models.TextField()
    Current = models.BooleanField()

