from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from senditapp.models import *

import jinja2
from jinja2.ext import loopcontrols

jinja_environ = jinja2.Environment(loader=jinja2.FileSystemLoader(['ui']), extensions=[loopcontrols])

def index(request):
	rider = Ride()
	template = loader.get_template('senditapp/index.html')
	Context = RequestContext(request, {'rider': rider})
	return HttpResponse(template.render(Context))
