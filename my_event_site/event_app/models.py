import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Event( models.Model ):
	name = models.CharField(max_length = 200)
	date = models.DateTimeField('date published')

	def __str__(self):
		return self.name

class Person( models.Model ):
	event = models.ForeignKey(Event, on_delete = models.CASCADE)
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	attendance_status = attendance_status = models.CharField(max_length = 10)

	def __str__(self):
		return self.first_name


