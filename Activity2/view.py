from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def page(request):
    return HttpResponse('<marquee>### Marc Nathaniel Santos ### BSIT 4B ### \n\n ACTIVITY 3 ### Mr. Darvin Evidor ###</marquee>')