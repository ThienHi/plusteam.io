from django import forms
from .models import Email

class EmailForms(forms.Form):
    name = forms.CharField(max_length=255)
    subject = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    content = forms.CharField()

    class Meta:
        modes = Email