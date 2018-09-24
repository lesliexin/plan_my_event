from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Event, Person, List, Guestlist, Item
from .forms import EventForm, ListForm, ItemForm, PersonForm

# Create your views here.
def event_list(request):
	events = Event.objects.all()
	return render(request, 'event_app/event_list.html', {'events': events} )

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    which_event = Event.objects.get(id=pk)
    lists = list(which_event.list_set.all())
    lists_ = which_event.list_set.all()
    guestlist = list(which_event.guestlist_set.all()[0].person_set.all())
    list_titles = []
    items = []
    item_list = []
    nums = []
    for indx, list_ in enumerate(lists):
        item_list = list(lists[indx].item_set.all())
        items.append(item_list)
        list_titles.append(list_.title)
        nums.insert(indx,indx)

    return render(request, 'event_app/event_detail.html', {
        'list_titles': list_titles, 
        'event': event, 
        'guestlist': guestlist, 
        'items': items,
        'nums': nums,
        'lists_': lists_,
        'which_event': which_event
    })

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
	return render(request,'event_app/event_edit.html', {'form': form, 'title': "New Event"})

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
    return render(request, 'event_app/event_edit.html', {'form': form, 'title': "Edit Event"})


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
    return render(request,'event_app/event_edit.html', {'form': form, 'title': "New List"})

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
    return render(request, 'event_app/event_edit.html', {'form': form, 'title': "Edit List"})

def list_detail(request, pk, pk2):
    event = get_object_or_404(Event, pk=pk)
    which_event = Event.objects.get(id=pk)
    lists = list(which_event.list_set.all())
    list_title = lists[pk2]
    which_list = which_event.list_set.get(title = list_title)   
    items_completed = which_list.item_set.filter(completed = True)
    items_not_completed = which_list.item_set.filter(completed = False)

    return render(request,'event_app/list_detail.html', {
        'items_completed': items_completed, 
        'items_not_completed': items_not_completed,
        'which_list': which_list,
        'event': event
    })

    return render(request,'event_app/list_detail.html')

def guestlist_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    which_event = Event.objects.get(id=pk)
    people = which_event.guestlist_set.get(title = 'Guest List')
    people_going = people.person_set.filter(will_attend = True)
    people_not_going = people.person_set.filter(will_attend = False)

    return render(request,'event_app/guestlist_detail.html', {
        'people_going': people_going, 
        'people_not_going': people_not_going,
        'event': event
    })

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
    return render(request,'event_app/event_edit.html', {'form': form, 'title': "New Item"})

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
    return render(request, 'event_app/event_edit.html', {'form': form, 'title': "Edit Item"})

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
    return render(request,'event_app/event_edit.html', {'form': form, 'title': "New Guest"})
   