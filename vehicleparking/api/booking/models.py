from django.db import models
from api.slot.models import Slot

class Booking(models.Model):
    slot=models.ForeignKey(Slot,on_delete=models.SET_NULL,blank=True,null=True)
    vehicle_no=models.CharField(max_length=25)
    price=models.CharField(max_length=50)
    start=models.DateTimeField(editable=True)
    end=models.DateTimeField(editable=True)
    phone=models.CharField(max_length=20)
    def __str__(self):
        return str(self.vehicle_no)+"---"+str(self.slot)
