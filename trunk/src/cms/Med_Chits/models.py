from django.db import models

# Create your models here.
class chit(models.Model):
    Mid = models.ForeignKey("MID.Mid")
    Diagnosis = models.TextField()
    Date_Start = models.DateField('Start Date')
    Date_End = models.DateField('End Date')
    DISPOSITION_CHOICES = (
                           ("SIQ","SIQ"),
                           ("CLA","SIQ with Class Option"),
                           )
    Disposition = models.CharField(max_length=3, choices=DISPOSITION_CHOICES)
    Admin_Notes = models.TextField()
    def __unicode__(self):
        return self.Mid + " - " + self.Diagnosis