from django.db import models

# Create your models here.

class Appartment(models.Model):
    address = models.CharField(max_length=40)
    habitants = models.IntegerField()

    def __unicode__(self):
        return self.address

class Habitant(models.Model):
    name = models.CharField(max_length=40)
    address = models.ForeignKey(Appartment)

    def __unicode__(self):
        return self.number

class Key(models.Model):
    number = models.IntegerField()
        
    def __unicode__(self):
        return self.number