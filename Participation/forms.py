from .models import Participant
from django import forms

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['full_name','educational_institution','phone','email']

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'forma',}),
            'educational_institution' : forms.TextInput(attrs={'class': 'forma',}),
            'phone': forms.TextInput(attrs={'class': 'forma mask_input_phone',
                                            'id':'phone',
                                            'v-model':'phone'}),
            'email': forms.TextInput(attrs={'class': 'forma',
                                            'id':'email',
                                            'v-model':'email'}),
        }