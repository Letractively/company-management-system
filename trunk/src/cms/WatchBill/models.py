from django.db import models

# Create your models here.
"""BILLET_CHOICES = (
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
REQUEST_TYPES = (
                 ('W','Weekend Liberty'),
                 ('D','Dining Out'),
                 ('L','Leave'),
                 ('O','Other'),
                 )
CHIT_REQUEST_LEVEL = (
                   ('SUPE','VADM M.H. Miller, USN'),
                   ('DANT','CAPT R.E. Clark II, USN'),
                   ('DDNT','CAPT B.P. O Donnell, USN'),
                   ('BATO','CAPT A. Jerrett, USN'),
                   ('CO','LT K. Igawa, USN'),
                   ('CSEL','AECS Morring, USN'),
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

class Uniform_Inspection(models.Model):
    #List of possible hits for a uniform inspection
    Inspector = models.ForeignKey(Mid)
    Room = models.CharField(max_length=4, choices=ROOM_CHOICES)
    Missing_items = models.BooleanField(False)
    Appearance = models.BooleanField()
    Grooming_Shave = models.BooleanField()
    Grooming_Length = models.BooleanField()
    Grooming_Appearance = models.BooleanField()
    Creases_present = models.BooleanField()
    Shined_shoes = models.BooleanField()
    IPs = models.BooleanField()
    Dust = models.BooleanField()
    Cover_dirt_ring = models.BooleanField()
    Cover_clean_bill = models.BooleanField()
    Shirt_undershirt = models.BooleanField()
    Shirt_proper_tie = models.BooleanField()
    Shirt_insignia_placement = models.BooleanField()
    Insignia_appearance = models.BooleanField()
    Belt_buckle_tip = models.BooleanField()
    Gig_line = models.BooleanField()
    Trousers_proper_length = models.BooleanField()
    ID_properly_displayed = models.BooleanField()
    Other = models.TextField()

class Weekend(models.Model):
    mid = models.ForeignKey(Mid)
    Startdate = models.DateField()
    Enddate = models.DateField()
    Location = models.CharField(max_length=40)
    ContactNumber = models.CharField(max_length=10)

class SpecialRequestChit(models.Model):
    mid = models.ForeignKey(Mid)
    Date = models.DateField()
    toLine = models.CharField(max_length=4, choices=CHIT_REQUEST_LEVEL)
    fromLine = models.CharField(max_length=50)
    viaLine = models.CharField(max_length=50)
    RequestType = models.CharField(max_length=1, choices=REQUEST_TYPES)
    otherRequestType = models.CharField(max_length=30)
    Justification = models.TextField()

class ORM_Chit(models.Model):
    mid = models.ForeignKey(Mid)
    L_Street1 = models.CharField(max_length=20)
    L_Street2 = models.CharField(max_length=20)
    L_City = models.CharField(max_length=30)
    L_State = models.CharField(max_length=2)
    l_Zip = models.CharField(max_length=5)
    Prim_Phone = models.CharField(max_length=10)
    Alt_Phone = models.CharField(max_length=10)
    DateDepart = models.DateField()
    DateReturn = models.DateField()
    Days_Travel = models.IntegerField()
    Days_Leave = models.IntegerField()
    Travel_Ratio = models.IntegerField()
    
class Leisure_Activites(models.Model):
    ORM_CHIT = models.ForeignKey(ORM_Chit)
    Activity = models.CharField(max_length=20)
    Duration = models.TimeField()
    RAC = models.IntegerField()
    
class Methods_of_Travel(models.Model):
    ORM_CHIT = models.ForeignKey(ORM_Chit)
    EstimatedDepartTime = models.DateTimeField()
    EstimatedArrivalTime = models.DateTimeField()
    Method_of_Travel = models.CharField(max_length=20)
    RAC = models.IntegerField()
    Risk_management_plan = models.TextField()
"""
class Form1(models.Model):
    FORM1_TYPE_CHOICES = (
                          ('P','Positive'),
                          ('N','Negative'),
                          )
    Form_Type = models.CharField(max_length=1, choices=FORM1_TYPE_CHOICES)
    Counseled_by = models.ForeignKey(Mid, related_name='+')
    Counseled_Billet = models.CharField(max_length=2, choices=BILLET_CHOICES)
    Counceling = models.ForeignKey(Mid, related_name='+')
    REASON_CHOICES = (
                      ('A','APPEARANCE'),
                      ('B','BEARING'),
                      ('MT','MOTIVATION'),
                      ('CP','COMPETENCE'),
                      ('PRO','PROFESSIONALISM'),
                      ('PHY','PHYSICAL ABILITY'),
                      ('D','DECISION MAKING'),
                      ('CM','COMMITMENT'),
                      ('MO','MORAL'),
                      )
    Reason = models.CharField(max_length=3, choices=REASON_CHOICES)
    Comment = models.TextField()
    RESOLUTION_CHOICES = (
                          ('C','Counseled'),
                          ('E','EMI awarded'),
                          ('C','Fwd for Commendation'),
                          ('A','Fwd for Adjudication'),
                          )
    Resolution = models.CharField(max_length=1,choices=RESOLUTION_CHOICES)
    
class Report0800(models.Model):
    Offgoing_CDO = models.ForeignKey(Mid, related_name='+')
    Oncoming_CDO = models.ForeignKey(Mid, related_name='+')
    Report_Date = models.DateField()
    FORCE_PROTECTION_CHOICES = (
                                ('A','Alpha'),
                                ('B','Bravo'),
                                ('C','Charlie'),
                                ('D','Delta'),                                
                                )
    Force_Protection_Condition = models.CharField(max_length=1, choices=FORCE_PROTECTION_CHOICES)

EVENT_TYPE_CHOICES = (
                     ('MMF','Morning Meal'),
                     ('NMF','Noon Meal Formation'),
                     ('EMF','Evening Meal Formation'),
                     ('TAP','TAPS'),
                     ('FOR','Forrestal Lecture'),
                     ('DRL','Drill'),
                     ('CAL','Officers Call'),
                     ('OTH','Other Special Event'),
                    )

ATTEND_STATUS_CHOICES = (
                         ('P','Present'),
                         ('A','Absent'),
                         ('U','Unauthorized Absent'),
                         ('E','Excused'),
                         )

WATCHBILL_TYPE_CHOICES = (
                          ('W','Work day'),
                          ('H','Holiday'),
                          )

WATCH_TYPE_CHOICES = (
                      ('CMDO','Company Mate of the Deck'),
                      ('ACDO','Asistant Company Duty Officer'),
                      ('CDO','Company Duty Officer'),
                      )

class Event(models.Model):
   DateTime = models.DateTimeField() 
   Type = models.CharField(max_length=3, choices=EVENT_TYPE_CHOICES)
   Location = models.CharField(max_length=30)
    
class Attendance(models.Model):
    Event = models.ForeignKey(Event) 
    Mid = models.ForeignKey(Mid)
    Status = models.CharField(max_length=1, choices=ATTEND_STATUS_CHOICES)
    Comment = models.TextField()
    Temp_Status = models.CharField(max_length=1, choices=ATTEND_STATUS_CHOICES)
    
class WatchBill(models.Model):
    Date = models.DateField()
    Type = models.CharField(max_length=1, choices=WATCHBILL_TYPE_CHOICES)
    
class Watch(models.Model):
    WatchBill = models.ForeignKey(WatchBill)
    Mid = models.ForeignKey(Mid)
    Post = models.CharField(max_length=20)
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    Type = models.CharField(max_length=4,choices=WATCH_TYPE_CHOICES)

    
