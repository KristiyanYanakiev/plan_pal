from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError

from .models import Proposal


class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        exclude = ['owner']
        widgets = {
            'participants': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'date_time': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['participants'].queryset = user.get_friends()
        else:
            self.fields['participants'].queryset = self.fields['participants'].queryset.none()

    def clean_date_time(self):
        dt = self.cleaned_data.get('date_time')

        if dt and dt < timezone.now():
            raise ValidationError("Invalid date")

        return dt