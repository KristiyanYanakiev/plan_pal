from django import forms

from proposals.models import Proposal


class ProposalForm(forms.ModelForm):

    class Meta:
        model = Proposal
        exclude = ['attendees', 'created_at', 'updated_at']
