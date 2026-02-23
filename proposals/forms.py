from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from proposals.models import Proposal

class ProposalSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        required=False
    )

class ProposalForm(forms.ModelForm):

    class Meta:
        model = Proposal
        exclude = ['participants', 'created_at', 'updated_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'type_of_activity': forms.TextInput(attrs={'class': 'form-control'}),
            'place_of_event': forms.URLInput(attrs={'class': 'form-control'}),
            'proposed_date_and_time': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),

        }


    def clean_proposed_date_and_time(self):
        date_time = self.cleaned_data.get('proposed_date_and_time')

        if date_time and date_time < timezone.now():
            raise ValidationError("You cannot schedule an event in the past.")

        return date_time

