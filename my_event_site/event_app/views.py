from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Event, Person, List, Guestlist
from .forms import EventForm, ListForm

# Create your views here.
def event_list(request):
	events = Event.objects.all()
	return render(request, 'event_app/event_list.html', {'events': events} )

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    which_event = Event.objects.get(id=pk)
    lists = list(which_event.list_set.all())
    guestlist = list(which_event.guestlist_set.all())
    list_titles = []
    items = []
    item_list = []
    nums = []
    for indx, list_ in enumerate(lists):
        item_list = list(lists[indx].item_set.all())
        items.append(item_list)
        list_titles.append(list_.title)
        nums.insert(indx,indx)
    length = len(list_titles)


    return render(request, 'event_app/event_detail.html', {
        'list_titles': list_titles, 
        'event': event, 
        'guestlist': guestlist, 
        'items': items,
        'length': length,
        'nums': nums
    })

def event_new(request):
	if request.method == "POST":
		form = EventForm(request.POST, instance=Event())
		if form.is_valid():
			event = form.save(commit=False)
			event.date = timezone.now()
			event.save()
			guestlist = Guestlist(title="Guest List", an_event=event)
			guestlist.save()
			return redirect('event_detail', pk=event.pk)
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


def list_new(request, pk):
    if request.method == "POST":
        event = get_object_or_404(Event, pk=pk)
        form = ListForm(request.POST, instance=List())
        if form.is_valid():
            list1 = form.save(commit=False)
            list1.an_event = event
            list1.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = ListForm()
    return render(request,'event_app/event_edit.html', {'form': form})