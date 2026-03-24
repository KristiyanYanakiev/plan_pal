from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils import timezone

from proposals.models import Proposal

User = get_user_model()


class ProposalSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        required=False
    )

class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        exclude = ['owner']
        widgets = {
            'participants': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['participants'].queryset = User.objects.exclude(id=user.id)


    def clean_proposed_date_and_time(self):
        date_time = self.cleaned_data.get('date_time')

        if date_time and date_time < timezone.now():
            raise ValidationError("You cannot schedule an event in the past.")

        return date_time

