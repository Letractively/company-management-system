#units models.py
# Author: Michael Harrison

from django.db import models

BATTALION_CHOICES = (
                     ('0','Brigade'),
                     ('1','1st Battalion'),
                     ('2','2nd Battalion'),
                     ('3','3rd Battalion'),
                     ('4','4th Battalion'),
                     ('5','5th Battalion'),
                     ('6','6th Battalion'),
                     )
CO_CHOICES = (
              ('1','1st Company'),
              ('2','2nd Company'),
              ('3','3rd Company'),
              ('4','4th Company'),
              ('5','5th Company'),
              ('6','6th Company'),
              ('7','7th Company'),
              ('8','8th Company'),
              ('9','9th Company'),
              ('10','10th Company'),
              ('11','11th Company'),
              ('12','12th Company'),
              ('13','13th Company'),
              ('14','14th Company'),
              ('15','15th Company'),
              ('16','16th Company'),
              ('17','17th Company'),
              ('18','18th Company'),
              ('19','19th Company'),
              ('20','20th Company'),
              ('21','21st Company'),
              ('22','22nd Company'),
              ('23','23rd Company'),
              ('24','24th Company'),
              ('25','25th Company'),
              ('26','26th Company'),
              ('27','27th Company'),
              ('28','28th Company'),
              ('29','29th Company'),
              ('30','30th Company'),              
              )

BILLET_CHOICES = (
                  ('DANT','Commendant of Midshipman'),
                  ('DDANT','Deputy Commendant of Midshipman'),
                  ('BO','Battalion Officer'),
                  ('CO','Company Officer'),
                  ('SEL','Company Senior Enlisted'),
                  )

class Rank(models.Model):
    rsNumber = models.IntegerField(max_length=2,null=True,blank=True)
    rank = models.CharField(max_length=20,null=True,blank=True,)

    def __unicode__(self):
        return u'%s' % (self.rank)

class Unit(models.Model):
    battalion = models.CharField(max_length=1,choices=BATTALION_CHOICES)
    company = models.CharField(max_length=2, choices=CO_CHOICES)
    firstClassCount = models.IntegerField(null=True,blank=True)
    secondClassCount = models.IntegerField(null=True,blank=True)
    thirdClassCount = models.IntegerField(null=True,blank=True)
    fourthClassCount = models.IntegerField(null=True,blank=True)
    unique_together = (("battalion", "company"),)

    def __unicode__(self):
        return u'%s company, %s Battalion' % (self.company,self.battalion)
    
class UnitLeader(models.Model):
    LName = models.CharField(max_length=30,null=True,blank=True)
    mName = models.CharField(max_length=3, null=True, blank=True)
    fName = models.CharField(max_length=30,null=True,blank=True)
    rank = models.ForeignKey('Rank.rank',null=True,blank=True)
    officePhone = models.CharField(max_length=10,null=True,blank=True)
    cellPhone = models.CharField(max_length=10,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    roomNumber = models.ForeignKey('mid.Room',null=True,blank=True)
    unit = models.ForeignKey(Unit,null=True,blank=True)
    billet = models.CharField(max_length=5,choices=BILLET_CHOICES,null=True,blank=True)
    
    def __unicode__(self):
        return u'%s %s' % (self.rank.rank,self.LName)
    
    
