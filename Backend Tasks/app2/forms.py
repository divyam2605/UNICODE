from django import forms

# class APIForm(forms.Form):
    Country = forms.CharField(max_length=100)
    Slug = forms.CharField(max_length=100)
    ISO2 = forms.CharField(max_length=100)