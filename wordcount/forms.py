from django import forms

#worcount form with the textfield
class WordCount(forms.Form):
    data = forms.CharField(required=True)
