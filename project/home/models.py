from django.db import models



class Trip(models.Model):
   tripId = models.IntegerField()
   source  = models.CharField(max_length=100)
   destination = models.CharField(max_length=100)
   date = models.CharField(max_length=100)
   trainNum = models.IntegerField()
   departureTime=models.CharField(max_length=100)
   arrivalTime=models.CharField(max_length=100)
   travelDuration=models.CharField(max_length=100)
   ticketPrice =models.DecimalField(max_digits=6,decimal_places=2)
   def __str__(self):
      return self.source +"-"+ self.destination



class Passenger(models.Model):
   name = models.CharField(max_length=100)
   email = models.CharField(max_length=100)
   phoneNum = models.CharField(max_length=11)
   tripId = models.IntegerField()
   trainNum = models.IntegerField()
   def __str__(self):
      return self.name

   

