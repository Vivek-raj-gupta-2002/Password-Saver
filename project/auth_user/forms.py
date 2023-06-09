from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#https://forum.djangoproject.com/t/can-i-apply-css-to-usercreationform/15632
class newUser(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            'email',
            
            'password1',
            'password2'
        )

    
        


class Login(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)