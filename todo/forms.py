from django import forms
from django.forms import fields
from .models import todoData


class todoForm(forms.ModelForm):
    class Meta:
        model = todoData
        fields = '__all__'
