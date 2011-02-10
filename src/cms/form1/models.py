from django.db import models

# Create your models here.
BILLET_CHOICES = (
    ('CC','Company Commander'),
    ('XO','Executive Officer'),
    ('HA','Honor Advisor'),
    ('OPS','Operations Officer'),
    ('ADJ','Adjutant'),
    ('PMO','Physical Mission Officer'),
    ('AC','Academics Officer'),
    ('SAF','Safety Officer'),
    ('A/C','Aptitude/Conduct Officer'),
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