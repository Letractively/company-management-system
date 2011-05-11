from django.db import models

FORM1_TYPE_CHOICES = (('P','Positive'),
                      ('N','Negative'),
                     )

REASON_CHOICES = (('A','APPEARANCE'),
                  ('B','BEARING'),
                  ('MT','MOTIVATION'),
                  ('CP','COMPETENCE'),
                  ('PRO','PROFESSIONALISM'),
                  ('PHY','PHYSICAL ABILITY'),
                  ('D','DECISION MAKING'),
                  ('CM','COMMITMENT'),
                  ('MO','MORAL'),
                 )

RESOLUTION_CHOICES = (('P', 'Pending'),
                      ('C','Counseled'),
                      ('E','EMI awarded'),
                      ('C','Fwd for Commendation'),
                      ('A','Fwd for Adjudication'),
                     )

class Form1(models.Model):
    mid = models.ForeignKey("mid.Mid")
    counseledBy = models.ForeignKey("mid.Mid", related_name='+')
    formType = models.CharField(max_length=1, choices=FORM1_TYPE_CHOICES)
    formDate = models.DateField('Form 1 Date and Time')
    reason = models.CharField(max_length=3, choices=REASON_CHOICES)
    comment = models.TextField()
    resolution = models.CharField(max_length=1,choices=RESOLUTION_CHOICES)
    def __unicode__(self):
        return self.formType + " - " + self.mid.LName + " - " + unicode(self.formDate)