from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Event, Person

# Create your views here.
def event_list(request):
	events = Event.objects.all()
	return render(request, 'event_app/event_list.html', {'events': events} )
