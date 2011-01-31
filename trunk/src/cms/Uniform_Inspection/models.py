from django.db import models

# Create your models here.
ROOM_CHOICES = (
    #Make in to Class
    ('6302','6302-2'),
    ('6303','6303-3'),
    ('6304','6304-3'),
    ('6305','6305-2'),
    ('6306','6306-2'),
    ('6307','6307-3'),
    ('6308','6308-4'),
    ('6309','6309-2'),
    ('6311','6311-3'),
    ('6314','6314-2'),
    ('6315','6315-3'),
    ('6316','6316-3'),
    ('6317','6317-3'),
    ('6318','6318-3'),
    ('6319','6319-3'),
    ('6320','6320-3'),
    ('6322','6322-2'),
    ('6323','6323-3'),
    ('6329','6329-3'),
    ('6402','6402-3'),
    ('6403','6403-2'),
    ('6404','6404-2'),
    ('6405','6405-2'),
    ('6406','6406-2'),
    ('6407','6407-2'),
    ('6408','6408-3'),
    ('6409','6409-2'),
    ('6411','6411-4'),
    ('6413','6413-2'),
    ('6414','6414-2'),
    ('6415','6415-2'),
    ('6416','6416-2'),
    ('6417','6417-2'),
    ('6418','6418-2'),
    ('6419','6419-2'),
    ('6420','6420-2'),
    ('6421','6421-3'),
    ('6425','6425-4'),
    ('6428','6428-2'),
    ('6429','6429-2'),
    ('6430','6430-2'),
    ('6431','6431-2'),
    ('6432','6432-2'),
    ('6433','6433-2'),
    ('6434','6434-2'),
    ('6435','6435-2'),
    ('6437','6437-2'),
    ('6438','6438-3'),
    ('6439','6439-2'),
    ('6440','6440-2'),
    ('6441','6441-4'),
    ('6443','6443-2'),
    ('6444','6444-2'),
    ('6445','6445-2'),
    ('6446','6446-2'),
    ('6455','6455-4'),
    ('6459','6459-2'),
    ('6460','6460-3'),
    ('6461','6461-2'),
    ('6462','6462-2'),
    ('6463','6463-2'),
    ('6464','6464-2'),
    ('6466','6466-3'),
    )
class Uniform_Inspection(models.Model):
    #List of possible hits for a uniform inspection
    Inspector = models.ForeignKey("MID.Mid")
    Room = models.CharField(max_length=4, choices=ROOM_CHOICES)
    DateTime = models.DateTimeField()
    Missing_items = models.BooleanField(False)
    Appearance = models.BooleanField()
    Grooming_Shave = models.BooleanField()
    Grooming_Length = models.BooleanField()
    Grooming_Appearance = models.BooleanField()
    Creases_present = models.BooleanField()
    Shined_shoes = models.BooleanField()
    IPs = models.BooleanField()
    Dust = models.BooleanField()
    Cover_dirt_ring = models.BooleanField()
    Cover_clean_bill = models.BooleanField()
    Shirt_undershirt = models.BooleanField()
    Shirt_proper_tie = models.BooleanField()
    Shirt_insignia_placement = models.BooleanField()
    Insignia_appearance = models.BooleanField()
    Belt_buckle_tip = models.BooleanField()
    Gig_line = models.BooleanField()
    Trousers_proper_length = models.BooleanField()
    ID_properly_displayed = models.BooleanField()
    Other = models.TextField()
    def __unicode_(self):
        return self.Room + " - " + self.DateTime
