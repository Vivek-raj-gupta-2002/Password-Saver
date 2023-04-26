from django import forms
from . import models


class addPassword(forms.ModelForm):
    class Meta:
        model = models.Passwords
        exclude = [
            'creater'
        ]

    