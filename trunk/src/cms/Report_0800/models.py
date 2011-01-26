from django.db import models

# Create your models here.

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
