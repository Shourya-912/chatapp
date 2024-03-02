import datetime
from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length = 1000)

class Message(models.Model):
    value = models.CharField(max_length = 10000000)
    date = models.DateTimeField(default = datetime.datetime.now, blank = True)
    room = models.CharField(max_length = 10000000)
    user = models.CharField(max_length=10000000)


