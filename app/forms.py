from django import forms
from django.forms import formset_factory


class DataForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'required': True}))


DataFormset = formset_factory(DataForm, extra=1, absolute_max=1100)
