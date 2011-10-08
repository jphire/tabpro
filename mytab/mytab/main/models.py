from django.db import models

# Create your models here.

class House(models.Model):
    road = models.CharField(max_length=40)
    number = models.CharField(max_length=5)
    real_estate_agency = models.CharField(max_length=40, blank=True)

    def __unicode__(self):
        return self.road + " " + self.number 
    
class Appartment(models.Model):
    road = models.ForeignKey(House, to_field=House.road, unique_together=True)
    road_number = models.ForeignKey(House, to_field=House.number, unique_together=True)
    stair = models.CharField(max_length=2, unique_together=True)
    appartment_number = models.IntegerField(unique_together=True)
        
    def __unicode__(self):
        return self.road + " " + self.road_number + " " + self.stair + " " + self.appartment_number

class Habitant(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    social_security = models.CharField(11)
    house = models.ForeignKey(House, blank=True)
    appartment = models.ForeignKey(Appartment, blank=True)
    phone = models.IntegerField(blank=True)

    def __unicode__(self):
        return self.first_name + " " + self.last_name

class Key(models.Model):
    key_id = models.IntegerField(primary_key=True)
    appartment = models.ForeignKey(Appartment)
    owner = models.ForeignKey(Habitant, blank=True)
    key_acquired_date = models.DateField()
    key_given_back_date = models.DateField()
    
    def __unicode__(self):
        return self.key_id
    
class TargetOfReservation(models.Model):
    house = models.ForeignKey(House)
    name = models.CharField(30)
    info = models.TextField()
    
    def __unicode__(self):
        return self.house + "/" + self.name
    
class Reservation(models.Model):
    number = models.IntegerField(primary_key=True)
    maker = models.ForeignKey(Habitant)
    created_date = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    def __unicode__(self):
        return self.number + " created:" + self.created_date

class Employee(models.Model):
    name = models.CharField(max_length=40)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True)
    
    def __unicode__(self):
        return self.name

class WorkOrder(models.Model):
    order_creator = models.ForeignKey(Employee)
    order_finisher = models.ForeignKey(Employee, blank=True)
    target = models.CharField(max_length=40)
    info = models.TextField()
    order_made_date = models.DateTimeField()
    work_done_date = models.DateTimeField()
    
    def __unicode__(self):
        return self.pk