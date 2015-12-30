from __future__ import unicode_literals

from django.db import models
from django import forms

#time_widget = forms.widgets.TimeInput(attrs={'class': 'time-pick'})
#valid_time_formats = ['%H:%M', '%I:%M%p', '%I:%M %p']

class Ride(models.Model):
	#pickup
    pick = models.CharField(max_length=300)
	#drop
    drop = models.CharField(max_length=300)
	#type of vehicle, time, mobile
    vehicle = models.CharField(max_length=300)
	#time
    time = models.TimeField()
    #widget=time_widget, help_text='ex: 10:30AM', input_formats=valid_time_formats
    
    #mobile
    mobile = models.IntegerField()