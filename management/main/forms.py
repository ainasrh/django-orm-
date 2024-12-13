from django import forms
from django.contrib.auth.models import User
from .models import project


class reg_form(forms.Form):
    username=forms.CharField(max_length=200)
    email=forms.EmailField( required=False)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    widget={
        'username': forms.TextInput(attrs={'class':'form-control'}),
        'email': forms.TextInput(attrs={'class':'form-control'}),
        'password': forms.TextInput(attrs={'class':'form-control'}),
        'confirm_password': forms.TextInput(attrs={'class':'form-control'}),

    }

class login_form(forms.Form):   
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)

class project_form(forms.ModelForm):
    class Meta:
        model=project
        fields='__all__'
