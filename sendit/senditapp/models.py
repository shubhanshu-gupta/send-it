from __future__ import unicode_literals

from django.db import models
from django import forms
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
#from location_field.models.spatial import LocationField
from geoposition.fields import GeopositionField

#time_widget = forms.widgets.TimeInput(attrs={'class': 'time-pick'})
#valid_time_formats = ['%H:%M', '%I:%M%p', '%I:%M %p']

class Ride(models.Model):
	#pickup
    pick = models.CharField(max_length=300)
    #location = LocationField(based_fields=[pick], zoom=7, default='Point(1.0 1.0)')
    #objects = models.GeoManager()
	position = GeopositionField()
    #drop
    drop = models.CharField(max_length=300)
    #location = LocationField(based_fields=[drop], zoom=7, default='Point(1.0 1.0)')
	#type of vehicle, time, mobile
    vehicle = models.CharField(max_length=300)
	#time
    time = models.TimeField()
    #widget=time_widget, help_text='ex: 10:30AM', input_formats=valid_time_formats
    #mobile
    mobile = models.IntegerField()


# class Place(models.Model):
#     city = models.CharField(max_length=255)
#     location = LocationField(based_fields=[city], zoom=7, default='Point(1.0 1.0)')
#     objects = models.GeoManager()