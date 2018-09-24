from django import forms

from .models import Event, List, Item, Person 

class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ('title',)


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('full_name', 'will_attend',)

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('title', 'priority', 'completed',)


class EventForm(forms.ModelForm):
  
    class Meta:
        model = Event
        fields = ('name', 'date')

