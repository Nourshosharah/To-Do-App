
from django import forms
from .models import *
  
class TodoForm(forms.ModelForm):
    class Meta:
        model = TO_DO
        fields="__all__"