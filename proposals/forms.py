from django import forms

from proposals.models import Proposal


class ProposalForm(forms.ModelForm):

    class Meta:
        model = Proposal
        exclude = ['attendees', 'created_at', 'updated_at']
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
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
