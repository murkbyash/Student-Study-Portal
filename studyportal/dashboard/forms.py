from django import forms
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from .models import *



class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']
