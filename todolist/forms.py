from django import forms
from django.forms import ModelForm

from .models import TodoList,TodoStatus

class DateInput(forms.DateInput):
    input_type = 'date'


class TodoForm(ModelForm):

    class Meta:
        model = TodoList
        fields = ['title', 'memo', 'duedate','status']
        widgets = {
            'duedate': DateInput(),
            'status':forms.Select(attrs={'class':'form-control'}),
            'status':forms.RadioSelect
        }

