from django import forms

from votes.models import Vote


class VoteForm(forms.ModelForm):

    class Meta:
        model = Vote
        fields = ['yes']
