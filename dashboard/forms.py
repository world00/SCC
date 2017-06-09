from django import forms
from dashboard.models import sht


class shtForm(forms.Form):
    shts = forms.ModelChoiceField(queryset=sht.objects.all().order_by('date'))
    