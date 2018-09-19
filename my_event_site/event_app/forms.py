from django import forms

from .models import Event, List

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('name',)


class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ('title',)