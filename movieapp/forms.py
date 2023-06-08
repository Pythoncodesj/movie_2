from.models import Movie
from django import forms
class Modelform(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','desc','img','year']
