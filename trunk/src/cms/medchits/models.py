from django.db import models

# Create your models here.
class Chit(models.Model):
    mid = models.ForeignKey("MID.Mid")
    diagnosis = models.TextField()
    dateStart = models.DateField('Start Date')
    dateEnd = models.DateField('End Date')
    DISPOSITION_CHOICES = (
                           ("SIQ","SIQ"),
                           ("CLA","SIQ with Class Option"),
                           )
    disposition = models.CharField(max_length=3, choices=DISPOSITION_CHOICES)
    adminNotes = models.TextField()
    def __unicode__(self):
        return self.Mid + " - " + self.Diagnosis