from django.forms import ModelForm
from .models import Users
from django import forms


class UserRegistrationForm(ModelForm):
    class Meta:
        model = Users
        fields = [
            'name',
            'phNumber',
            'Email',
            'password',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control ', 'required': 'True', 'autocomplete': "off"}),
            'phNumber': forms.NumberInput(attrs={'class': 'form-control', 'required': 'True', 'autocomplete': "off"}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'True', 'autocomplete': "off"}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'required': 'True', 'autocomplete': "off"})
        }
        labels = {
            'name': 'Name',
            'phNumber': 'Phone Number',
            'Email': 'Email',
            'password': 'Password'
        }
