from django.db import models

# Create your models here.
WATCHBILL_TYPE_CHOICES = (
                          ('W','Work day'),
                          ('H','Holiday'),
                          ('L','Leave')
                          )

WATCH_TYPE_CHOICES = (
                      ('CMDO','Company Mate of the Deck'),
                      ('ACDO','Asi.edstant Company Duty Officer'),
                      ('CDO','Company Duty Officer'),
                      )
Ac_WEEK_CHOICES = (
                   ('B','Blue Week'),
                   ('G','Gold Week'),
                   )
Ac_WEEK_START = (
                 ('E','Even'),
                 ('O','Odd'),            
                 )
SEMESTER_CHOICES = (
                    ('F','Fall'),
                    ('S','Spring'),
                    )
DAY_CHOICES = (
               ('0','Sunday'),
               ('1','Monday'),
               ('2','Tuesday'),
               ('3','Wednesday'),
               ('4','Thursday'),
               ('5','Friday'),
               ('6','Saturday'),
               )
DS_CHOICES = (
    ('1','Duty Section 1'),
    ('2','Duty Seciton 2'),
    ('3','Duty Section 3'),
    ('4','Duty Section 4'),
    ('5','Duty Section 5'),
    ('6','Duty Section 6'),
    ('7','Duty Section 7'),
    ('8','Duty Section 8'),
    ('O','Out of Company'),              
              )

AcYearChoices = (
                 (11,'2010-2011'),
                 (12,'2011-2012'),
                 (13,'2012-2013'),
                 (14,'2013-2014'),
                 (15,'2014-2015'),
                 (16,'2015-2016'),
                 (17,'2016-2017'),
                 (18,'2017-2018'),
                 (19,'2018-2019'),
                 (20,'2019-2020'),
                 (21,'2020-2021'),
                 )

class AcYear(models.Model):
    acYear = models.IntegerField(max_length=2,choices=AcYearChoices)
    isInit = models.NullBooleanField(null=True,blank=True)   
    fallStart = models.DateField(null=True,blank=True)
    fallGoldWeekStart = models.CharField(max_length=1, choices=Ac_WEEK_START,null=True,blank=True)
    fall6Weeks = models.DateField(null=True,blank=True)
    fall12Weeks = models.DateField(null=True,blank=True)
    thanksgivingStart = models.DateField(null=True,blank=True)
    thanksgivingEnd = models.DateField(null=True,blank=True)
    fallXWeekStart = models.DateField(null=True,blank=True)
    fallXWeekEnd = models.DateField(null=True,blank=True)
    christmasStart = models.DateField(null=True,blank=True)
    christmasEnd = models.DateField(null=True,blank=True)
    christmasIntersessionalStart = models.DateField(null=True,blank=True)
    christmasIntersessionalEnd = models.DateField(null=True,blank=True) 
    laborDay = models.DateField(null=True,blank=True)
    columbusDay = models.DateField(null=True,blank=True)
    veteransDay = models.DateField(null=True,blank=True)    
    fallEnd = models.DateField(null=True,blank=True)    
    startSpring = models.DateField(null=True,blank=True)
    spring6Weeks = models.DateField(null=True,blank=True)
    spring12Weeks = models.DateField(null=True,blank=True)
    springXWeekStart = models.DateField(null=True,blank=True)
    springXWeekEnd = models.DateField(null=True,blank=True)
    springBreakStart = models.DateField(null=True,blank=True)
    springBreakEnd = models.DateField(null=True,blank=True)
    mlkDay = models.DateField(null=True,blank=True)
    washingtonBirthday = models.DateField(null=True,blank=True)   
    springEnd = models.DateField(null=True,blank=True)
    springIntersessionalStart = models.DateField(null=True,blank=True)
    springIntersessionalEnd = models.DateField(null=True,blank=True)
    summerStart = models.DateField(null=True,blank=True)
    def __unicode__(self):
        return "20" + str(self.acYear-1) + " - 20" + str(self.acYear)
    
class AcWatch(models.Model):
    acYear = models.ForeignKey(AcYear)
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES)
    week = models.CharField(max_length=1, choices=SEMESTER_CHOICES)
    dayOfWeek = models.IntegerField(max_length=1, choices=DAY_CHOICES)
    startTime = models.TimeField()
    mid = models.ForeignKey("mid.Mid")
    def __unicode__(self):
        return unicode(self.semester) + unicode(self.acYear)
    

class WatchBill(models.Model):
    date = models.DateField('Watchbill Date')
    type = models.CharField(max_length=1, choices=WATCHBILL_TYPE_CHOICES)
    dutySection = models.CharField(max_length=1, choices=DS_CHOICES, null=True, blank=True)
    CDO = models.ForeignKey("mid.Mid", related_name='+')
    ACDO = models.ForeignKey("mid.Mid", related_name='+')
    def __unicode_(self):
        return self.type + " - " + unicode(self.date)
    
class Watch(models.Model):
    watchBill = models.ForeignKey(WatchBill)
    mid = models.ForeignKey("mid.Mid")
    post = models.CharField(max_length=20)
    startTime = models.TimeField()
    endTime = models.TimeField()
    type = models.CharField(max_length=4,choices=WATCH_TYPE_CHOICES)
    def __unicode__(self):
        return self.mid.LName + " - " + self.watchBill + " - " + unicode(self.startTime)
    
class LogBook(models.Model):
    watchBill = models.ForeignKey(WatchBill)
    
class LogEntry(models.Model):
    watch = models.ForeignKey(LogBook)
    entryTime = models.TimeField()
    entry = models.TextField()
    def __unicode__(self):
        return unicode(self.LogBook.watchBill) + unicode(self.entryTime)
    
