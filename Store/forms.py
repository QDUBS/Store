from django import forms
from django.forms import ModelForm
from .models import Item




TYPE_CHOICES = (
    ('-', '-'),
    ('+', '+'),
    ('--', '--'),
)

class ItemForm(forms.ModelForm):
    type = forms.ChoiceField(choices = TYPE_CHOICES, widget=forms.Select(attrs={'placeholder': ''}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ADD DESCRIPTION'}))
    value = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'VALUE'}))

    class Meta:
        model = Item
        fields = ['type', 'description', 'value']
