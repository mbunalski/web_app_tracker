from django.db import models

# Create your models here.
class shift_event(models.Model):
    type_activity = models.CharField(max_length=20)
    time_activity =  models.IntegerField(default=0)