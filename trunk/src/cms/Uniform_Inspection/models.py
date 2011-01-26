from django.db import models

# Create your models here.
class Uniform_Inspection(models.Model):
    #List of possible hits for a uniform inspection
    Inspector = models.ForeignKey("MID.Mid")
    Room = models.CharField(max_length=4, choices="MID.ROOM_CHOICES")
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
