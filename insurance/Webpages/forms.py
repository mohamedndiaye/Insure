from django import forms
from .models import Bmi, Wth

class BmiForm(forms.Form):
    name = forms.CharField(required=False)
    height = forms.FloatField(label="Height in m:", required=True, min_value=0)
    weight = forms.FloatField(label="Weight in kg:", required=True, min_value=0)

class BmiMeasurementForm(forms.ModelForm):
    class Meta:
        model = Bmi
        fields = ["id", "height", "weight"]

class WthForm(forms.Form):
    name = forms.CharField(required=False)
    waist = forms.FloatField(label="Waist measurement in cms:", required=True, min_value=0)
    hip = forms.FloatField(label="Hip measurement in cms:", required=True, min_value=0)

class WthMeasurementForm(forms.ModelForm):
    class Meta:
        model = Wth
        fields = ["id", "waist", "hip"]
