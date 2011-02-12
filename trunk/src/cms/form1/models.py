from django.db import models


class Form1(models.Model):
    FORM1_TYPE_CHOICES = (
                          ('P','Positive'),
                          ('N','Negative'),
                          )
    formType = models.CharField(max_length=1, choices=FORM1_TYPE_CHOICES)
    dateTime = models.DateTimeField('Form 1 Date and Time')
    counseledBy = models.ForeignKey("mid.Mid", related_name='+')
    counseledBillet = models.CharField(max_length=2, choices=BILLET_CHOICES)
    counseling = models.ForeignKey("mid.Mid", related_name='+')
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
    reason = models.CharField(max_length=3, choices=REASON_CHOICES)
    comment = models.TextField()
    RESOLUTION_CHOICES = (
                          ('C','Counseled'),
                          ('E','EMI awarded'),
                          ('C','Fwd for Commendation'),
                          ('A','Fwd for Adjudication'),
                          )
    resolution = models.CharField(max_length=1,choices=RESOLUTION_CHOICES)
    def __unicode__(self):
        return self.Form_Type + " - " + self.DateTime