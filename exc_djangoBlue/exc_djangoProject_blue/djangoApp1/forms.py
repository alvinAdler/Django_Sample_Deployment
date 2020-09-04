from django import forms
#pylint: disable=imported-auth-user
from django.contrib.auth.models import User
from djangoApp1.models import Basic_User_Model

class Basic_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")

class Additional_Form(forms.ModelForm):
    class Meta():
        model = Basic_User_Model
        fields = ("basic_portfolio_site", "basic_profpict")