from django.shortcuts import render
from django.http import HttpResponse

from senditapp.models import *

import jinja2
from jinja2.ext import loopcontrols

jinja_environ = jinja2.Environment(loader=jinja2.FileSystemLoader(['ui']), extensions=[loopcontrols])

def index(request):
	return HttpResponse("Hello World!")
