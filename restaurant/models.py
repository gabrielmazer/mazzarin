from django.db import models

# Create your models here.
class Menu(models.Model):
   title = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   inventory = models.SmallIntegerField(default=5) 

   def __str__(self):
      return f'{self.title} : {"$"+str(self.price)}'


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return f'{self.first_name} : {str(self.reservation_date)} : {self.reservation_slot} guests'
    
