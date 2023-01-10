from django import forms
from .models import People

class Peopledetails(forms.ModelForm):
    class Meta:
        model = People
        fields = '__all__'
        labels = {'details':''}