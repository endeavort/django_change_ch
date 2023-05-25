from django import forms


class TextForm(forms.Form):
    text = forms.CharField()
    search = forms.CharField()
    replace = forms.CharField()
