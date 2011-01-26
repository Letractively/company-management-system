from django.db import models

# Create your models here.

class Form1(models.Model):
    FORM1_TYPE_CHOICES = (
                          ('P','Positive'),
                          ('N','Negative'),
                          )
    Form_Type = models.CharField(max_length=1, choices=FORM1_TYPE_CHOICES)
    Counseled_by = models.ForeignKey("MID.Mid", related_name='+')
    Counseled_Billet = models.CharField(max_length=2, choices=BILLET_CHOICES)
    Counceling = models.ForeignKey("MID.Mid", related_name='+')
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