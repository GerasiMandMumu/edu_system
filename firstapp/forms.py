from django import forms
from django.forms import ModelForm

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['login', 'password', 'user']