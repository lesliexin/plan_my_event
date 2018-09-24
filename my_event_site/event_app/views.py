from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Event, Person, List, Guestlist, Item
from .forms import EventForm, ListForm, ItemForm, PersonForm

# displays list of events
def event_list(request):
	events = Event.objects.all()
	return render(request, 'event_app/event_list.html', {
        'events': events
    })

# displays the lists in an event and the items in each list
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    lists_ = which_event.list_set.all()
    guestlist = list(event.guestlist_set.all()[0].person_set.all())

    return render(request, 'event_app/event_detail.html', { 
        'event': event, 
        'guestlist': guestlist, 
        'lists_': lists_,
    })

# creates a new event instance
# redirects to 'event_detail' page
# generates empty guestlist
def event_new(request):
	if request.method == "POST":
		form = EventForm(request.POST, instance=Event())
		if form.is_valid():
			event = form.save(commit=False)
			event.save()
			guestlist = Guestlist(title="Guest List", an_event=event)
			guestlist.save()
			return redirect('event_detail', pk=event.pk)
	else:
		form = EventForm()
	return render(request,'event_app/event_edit.html', {
        'form': form,
        'title': "New Event"
    })

# edits fields in an existing event
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
    
    return render(request, 'event_app/event_edit.html', {
        'form': form,
        'title': "Edit Event"
    })

# creates a new list instance
# redirects to 'event_detail' page
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
    return render(request,'event_app/event_edit.html', {
        'form': form,
        'title': "New List"
    })

# edits fields in an existing list
def list_edit(request, pk, pk2):
    event = get_object_or_404(Event, pk=pk)
    list_ = get_object_or_404(List, pk=pk2)
    if request.method == "POST":
        form = ListForm(request.POST, instance=list_)
        if form.is_valid():
            list_ = form.save(commit=False)
            list_.an_event = event
            list_.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = ListForm(instance=list_)
    return render(request, 'event_app/event_edit.html', {
        'form': form,
        'title': "Edit List"
    })

# displays the events in a specific list
def list_detail(request, pk, pk2):
    event = get_object_or_404(Event, pk=pk)
    which_list = event.list_set.get(id=pk2)
    items_completed = which_list.item_set.filter(completed = True)
    items_not_completed = which_list.item_set.filter(completed = False)

    return render(request,'event_app/list_detail.html', {
        'items_completed': items_completed, 
        'items_not_completed': items_not_completed,
        'which_list': which_list,
        'event': event
    })

    return render(request,'event_app/list_detail.html')

# displays the guests in a guestlist
def guestlist_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    people = event.guestlist_set.get(title = 'Guest List')
    people_going = people.person_set.filter(will_attend = True)
    people_not_going = people.person_set.filter(will_attend = False)

    return render(request,'event_app/guestlist_detail.html', {
        'people_going': people_going, 
        'people_not_going': people_not_going,
        'event': event
    })

# creates a new item instance 
# redirects to 'event_detail' page
def item_new(request, pk, pk2):
    if request.method == "POST":
        event = get_object_or_404(Event, pk=pk)
        list_ = get_object_or_404(List, pk=pk2)
        form = ItemForm(request.POST, instance=Item())
        if form.is_valid():
            item = form.save(commit=False)
            item.a_list = list_
            item.created_date = timezone.now()
            item.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = ItemForm()
    return render(request,'event_app/event_edit.html', {
        'form': form,
        'title': "New Item"
    })

# edits fields in an existing item
def item_edit(request, pk, pk2, pk3):
    event = get_object_or_404(Event, pk=pk)
    list_ = get_object_or_404(List, pk=pk2)
    item = get_object_or_404(Item, pk=pk3)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.a_list = list_
            item.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'event_app/event_edit.html', {
        'form': form,
        'title': "Edit Item"
    })

# creates a new person instance 
# redirects to 'event_detail' page
def person_new(request, pk):
    if request.method == "POST":
        event = get_object_or_404(Event, pk=pk)
        guestlist = event.guestlist_set.all()[0]
        form = PersonForm(request.POST, instance=Person())
        if form.is_valid():
            person = form.save(commit=False)
            person.a_list = guestlist
            person.created_date = timezone.now()
            person.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = PersonForm()
    return render(request,'event_app/event_edit.html', {
        'form': form,
        'title': "New Guest"
    })
   