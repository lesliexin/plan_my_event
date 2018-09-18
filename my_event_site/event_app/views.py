from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Event, Person, List
from .forms import EventForm, ListForm

# Create your views here.
def event_list(request):
	events = Event.objects.all()
	return render(request, 'event_app/event_list.html', {'events': events} )

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    lists1 = Event.objects.get(id=pk)
    lists = list(lists1.list_set.all())

    return render(request, 'event_app/event_detail.html', {'lists': lists, "event": event})

def event_new(request):
	if request.method == "POST":
		form = EventForm(request.POST)
		# form_list = ListForm(request.POST)
		if form.is_valid():
			event = form.save(commit=False)
			event.date = timezone.now()
			event.save()
			# list1 = form_list.save(commit=False)
			# list1.save()
			list1 = List(title="Guest List", an_event=event)
			list1.save()

			return redirect('event_list')
	else:
		form = EventForm()
	return render(request,'event_app/event_edit.html', {'form': form})

def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.date = timezone.now()
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'event_app/event_edit.html', {'form': form})