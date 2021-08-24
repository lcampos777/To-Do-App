from django import forms
from django.forms.widgets import TextInput
from .models import ToDo

class ToDoForm(forms.ModelForm):
    class Meta():
        model = ToDo
        fields = "__all__"

class InputForm(forms.Form):

    STATE_CHOICES = (
        ("Open","Open"),
        ("On Course","On Course"),
        ("Completed","Completed"),
    )

    title = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class":"form", "placeholder":"Title"}))
    description = forms.CharField(max_length=500, required=True, widget=forms.Textarea(attrs={"class":"form", "placeholder":"Description"}))
    state = forms.ChoiceField(choices=STATE_CHOICES, required=True, widget=forms.Select(attrs={"class":"form"}))
    date = forms.DateField(widget=forms.SelectDateWidget(attrs={"class":"form"}))