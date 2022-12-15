from django import forms
from django.forms import ModelForm
from .models import appointment
from .models import applyToGrad

class appointmentForm(ModelForm):
    class Meta:
        model = appointment
        fields = ('redID', 'advisor')
        widgets = {
            'redID': forms.TextInput(attrs={'class':'form-control'}),
            'advisor': forms.TextInput(attrs={'class':'form-control'})
        }

class applyGradForm(ModelForm):
    class Meta:
        model = applyToGrad
        fields = ('firstName', 'lastName', 'redID', 'catalogYear', 'major')
        widgets = {
            'firstName': forms.TextInput(attrs={'class':'form-control'}),
            'lastName': forms.TextInput(attrs={'class':'form-control'}),
            'redID': forms.TextInput(attrs={'class':'form-control'}),
            'catalogYear': forms.TextInput(attrs={'class':'form-control'}),
            'major': forms.TextInput(attrs={'class':'form-control'}),
        }