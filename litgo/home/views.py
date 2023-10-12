from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.

def index(request):
    now = datetime.datetime.now()
    html = "<html><body><p>Coming Soon Project Sedang Dikembangkan</p><br/>It is now %s.</body></html>" % now
    return HttpResponse(html)
