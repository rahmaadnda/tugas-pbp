from django import forms
from .models import Task

class Input_Form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description",]
        labels = {'title': "title", "description": "description",}