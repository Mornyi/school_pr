from django import forms
from .models import Record

class RecordForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Напишите что-нибудь...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",)

    class Meta:
        model = Record
        exclude = ("user", )