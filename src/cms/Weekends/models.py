from django.db import models

# Create your models here.
STATUS_CHOICES = (
                  ('P','Pending'),
                  ('A','Approved'),
                  ('D','Disapproved'),
                  )
class Weekend(models.Model):
    mid = models.ForeignKey("MID.Mid")
    Startdate = models.DateField()
    Enddate = models.DateField()
    Status = models.CharField(maxlength=1,choices=STATUS_CHOICES)
    Location = models.CharField(max_length=40)
    ContactNumber = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.mid + " - " + self.Startdate