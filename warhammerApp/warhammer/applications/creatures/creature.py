from django.db import models
from multiselectfield import MultiSelectField
from django.urls import reverse


# Create your models here.
class Creature(models.Model):
    name = models.CharField(max_length=50, unique=True)
    WW   = models.IntegerField()
    US   = models.IntegerField()
    K    = models.IntegerField()
    Odp  = models.IntegerField()
    Zr   = models.IntegerField()
    Int  = models.IntegerField()
    SW   = models.IntegerField()
    Ogd  = models.IntegerField()
    A    = models.IntegerField()
    Zyw  = models.IntegerField()
    Sz   = models.IntegerField()
    Mag  = models.IntegerField()
    PO   = models.IntegerField()
    PP   = models.IntegerField()