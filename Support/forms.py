from django.forms import ModelForm
from .models import FeedBack
from django import forms


class UsersFeedBack(ModelForm):
    class Meta:
        model = FeedBack
        fields = [
            'name',
            'email',
            'GameName',
            'reportType',
            'comment'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control ', 'required': 'True', 'autocomplete': "off"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'True', 'autocomplete': "off"}),
            'GameName': forms.Select(attrs={'class': 'form-control', 'required': 'True', 'autocomplete': "off"}),
            'reportType': forms.Select(attrs={'class': 'form-control', 'required': 'True', 'autocomplete': "off"}),
            'comment': forms.Textarea(attrs={'class': 'form-control ', 'required': 'True', 'autocomplete': "off"}),
        }
        labels = {
            'name': "Name",
            'email': "Email",
            "GameName": "Select Game",
            "reportType": "Select Report Header",
            "comment": "FeedBack"
        }
