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

class AcYear(models.Model):
    fallStart = models.DateField()
    fallGoldWeekStart = models.CharField(max_length=1, choices=Ac_WEEK_START)
    fall6Weeks = models.DateField()
    fall12Weeks = models.DateField()
    thanksgivingStart = models.DateField()
    thanksgivingEnd = models.DateField()
    fallXWeekStart = models.DateField()
    fallXWeekEnd = models.DateField()
    christmasStart = models.DateField()
    christmasEnd = models.DateField()
    christmasIntersessionalStart = models.DateField()
    christmasIntersessionalEnd = models.DateField()    
    laborDay = models.DateField()
    columbusDay = models.DateField()
    veteransDay = models.DateField()    
    fallEnd = models.DateField()    
    startSpring = models.DateField()
    spring6Weeks = models.DateField()
    spring12Weeks = models.DateField()
    springXWeekStart = models.DateField()
    springXWeekEnd = models.DateField()
    springBreakStart = models.DateField()
    springBreakEnd = models.DateField()
    mlkDay = models.DateField()
    washingtonBirthday = models.DateField()   
    endSpring = models.DateField()
    springIntersessionalStart = models.DateField()
    springIntersessionalEnd = models.DateField()
    startSummer = models.DateField()
    
class AcWatch(models.Model):
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES)
    week = models.CharField(max_length=1, choices=SEMESTER_CHOICES)
    dayOfWeek = models.IntegerField(max_length=1, choices=DAY_CHOICES)
    startTime = models.TimeField()
    mid = models.ForeignKey("mid.Mid")
    

class WatchBill(models.Model):
    date = models.DateField('Watchbill Date')
    type = models.CharField(max_length=1, choices=WATCHBILL_TYPE_CHOICES)
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
    watch = models.ForeignKey(Watch)
    entry = models.TextField()
    
