from .models import Participant
from django import forms

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['full_name','educational_institution','phone','email']

        widgets = {
            'full_name' : forms.TextInput(attrs={'class': 'forma'}),
            'educational_institution' : forms.TextInput(attrs={'class': 'forma'}),
            'phone': forms.TextInput(attrs={'class': 'forma imaskjs__input_tel'}),
            'email': forms.TextInput(attrs={'class': 'forma'}),
        }