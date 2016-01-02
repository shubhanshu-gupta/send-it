from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from senditapp.models import *
import requests, json


import jinja2
from jinja2.ext import loopcontrols

jinja_environ = jinja2.Environment(loader=jinja2.FileSystemLoader(['ui']), extensions=[loopcontrols])

def index(request):
	rider = Ride()
	template = loader.get_template('senditapp/index.html')
	Context = RequestContext(request, {'rider': rider})
	return HttpResponse(template.render(Context))


finaldata=[]
@csrf_exempt
def show(request):
	rider = Ride()
	rider.pick = request.POST['pick_location']
	rider.drop = request.POST['drop_location']
	rider.vehicle = request.POST['vehicle_type']
	rider.time = request.POST['time']
	rider.mobile = request.POST['mobile_no']
	rider.save()
	
	#gmaps = GoogleMaps(AIzaSyCSYYYxo6vopZp8hOzpEMywRutTsMDoGIc)
	#lat, lng = gmaps.address_to_latlng(rider.pick)
	url = 'http://photon.komoot.de/api/?q='
	addresses_p = [rider.pick]
	addresses_d = [rider.drop]
	
	for address in addresses_p:
		resp = requests.get(url=url+address)
		data = json.loads(resp.text)
	
	cord_pick = data['features'][0]['geometry']['coordinates']
	
	for address in addresses_d:
		resp = requests.get(url=url+address)
		data = json.loads(resp.text)
	
	cord_drop = data['features'][0]['geometry']['coordinates']

	ridedata={}
	ridedata['pick_location']=rider.pick
	ridedata['drop_location']=rider.drop
	ridedata['vehicle_type']=rider.vehicle
	ridedata['time']=rider.time
	ridedata['mobile_no']=rider.mobile
	
	ridedata['pick_lat'] = cord_pick[0]
	ridedata['pick_lng'] = cord_pick[1]
	ridedata['drop_lat'] = cord_drop[0]
	ridedata['drop_lng'] = cord_drop[1]
	
	finaldata.append(ridedata)
	template = loader.get_template('senditapp/booked.html')
	Context = RequestContext(request, {'finaldata':finaldata})
	print "Final Data ", finaldata
	return HttpResponse(template.render(Context))
	#return render_to_response('senditapp/booked.html', {'finaldata': finaldata},  RequestContext(request))
