import datetime

from django.db import models
from django.utils import timezone

PRIORITY_CHOICES = ( 
  (1, 'Low'), 
  (2, 'Normal'), 
  (3, 'High'), 
) 

class Event( models.Model ):
	name = models.CharField(max_length = 200)
	date = models.DateTimeField('Date of event', default = timezone.now() + datetime.timedelta(days=7))

	def __str__(self):
		return self.name

class List(models.Model): 
  title = models.CharField(max_length=250, default="", unique=False) 
  an_event = models.ForeignKey(Event, on_delete = models.CASCADE) 

  def __str__(self): 
    return self.title 
  class Meta: 
    ordering = ['title'] 
  class Admin: 
    pass

class Guestlist(models.Model): 
  title = models.CharField(max_length=250, default="", unique=False) 
  an_event = models.ForeignKey(Event, on_delete = models.CASCADE) 

  def __str__(self): 
    return self.title 
  class Meta: 
    ordering = ['title'] 
  class Admin: 
    pass

class Person( models.Model ):
	a_list = models.ForeignKey(Guestlist, on_delete = models.CASCADE)
	full_name = models.CharField(max_length=50, default="") 
	created_date = models.DateTimeField(default=datetime.datetime.now) 
	will_attend = models.BooleanField(default=False)

	def __str__(self):
		return self.full_name
	class Meta:
		ordering = ['full_name'] 
	class Admin: 
		pass

class Item(models.Model): 
  title = models.CharField(max_length=250, default="") 
  created_date = datetime.datetime.now
  priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2) 
  completed = models.BooleanField(default=False) 
  a_list = models.ForeignKey(List, on_delete = models.CASCADE) 
  
  def __str__(self): 
    return self.title 
  class Meta: 
    ordering = ['-priority', 'title'] 
  class Admin: 
    pass
